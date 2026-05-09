"""
backend/routers/query.py

RAG query endpoint — the core API that AI agent builders call.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import chromadb
import os
import logging
from typing import Optional

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["query"])


def get_chroma_client():
    persist_dir = os.getenv("CHROMA_PERSIST_DIR", "./chroma_data")
    if os.getenv("CHROMA_HOST"):
        return chromadb.HttpClient(
            host=os.getenv("CHROMA_HOST", "localhost"),
            port=int(os.getenv("CHROMA_PORT", "8001")),
        )
    return chromadb.PersistentClient(path=persist_dir)


class QueryRequest(BaseModel):
    collection_id: str = Field(..., example="trading-strategy-expert-v1")
    query: str = Field(..., min_length=1, max_length=2000, example="What is the entry signal?")
    top_k: int = Field(default=5, ge=1, le=20)
    include_metadata: bool = Field(default=True)


class ChunkResult(BaseModel):
    text: str
    score: float
    chunk_index: Optional[int] = None
    source: Optional[str] = None
    metadata: Optional[dict] = None


class QueryResponse(BaseModel):
    collection_id: str
    query: str
    results: list[ChunkResult]
    total_chunks_searched: int


def distance_to_score(d: float) -> float:
    return round(max(0.0, 1.0 - d), 4)


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """
    Query a Ragify RAG package. Used by AI agent builders to retrieve
    relevant chunks from a creator's content.

    Example:
        POST /api/query
        {"collection_id": "my-rag-abc123", "query": "entry signal", "top_k": 5}
    """
    try:
        client = get_chroma_client()
    except Exception as e:
        logger.error(f"ChromaDB connection failed: {e}")
        raise HTTPException(status_code=503, detail="Vector database unavailable.")

    try:
        collection = client.get_collection(name=request.collection_id)
    except Exception:
        raise HTTPException(
            status_code=404,
            detail=f"RAG package '{request.collection_id}' not found.",
        )

    try:
        results = collection.query(
            query_texts=[request.query],
            n_results=min(request.top_k, collection.count()),
            include=["documents", "distances", "metadatas"],
        )
    except Exception as e:
        logger.error(f"Query failed: {e}")
        raise HTTPException(status_code=500, detail="Query failed. Please try again.")

    documents = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    chunks = []
    for i, (doc, dist, meta) in enumerate(zip(documents, distances, metadatas)):
        chunks.append(ChunkResult(
            text=doc,
            score=distance_to_score(dist),
            chunk_index=meta.get("chunk_index", i) if request.include_metadata else None,
            source=meta.get("source") if request.include_metadata else None,
            metadata={k: v for k, v in meta.items() if k not in ("chunk_index", "source")}
            if request.include_metadata and meta else None,
        ))

    chunks.sort(key=lambda c: c.score, reverse=True)

    return QueryResponse(
        collection_id=request.collection_id,
        query=request.query,
        results=chunks,
        total_chunks_searched=collection.count(),
    )


@router.get("/collections/{collection_id}/info")
async def get_collection_info(collection_id: str):
    """Returns metadata and chunk count for a RAG package."""
    try:
        client = get_chroma_client()
        collection = client.get_collection(name=collection_id)
    except Exception:
        raise HTTPException(status_code=404, detail=f"RAG package '{collection_id}' not found.")

    return {
        "collection_id": collection_id,
        "chunk_count": collection.count(),
        "metadata": collection.metadata or {},
    }


@router.get("/collections/{collection_id}/preview")
async def preview_collection(collection_id: str, query: str, top_k: int = 3):
    """
    Free preview — returns up to 3 truncated chunks so buyers can
    evaluate quality before purchasing.
    """
    req = QueryRequest(
        collection_id=collection_id,
        query=query,
        top_k=min(top_k, 3),
        include_metadata=False,
    )
    response = await query_rag(req)

    for chunk in response.results:
        cutoff = int(len(chunk.text) * 0.6)
        chunk.text = chunk.text[:cutoff] + "… [purchase to unlock full content]"

    return response
