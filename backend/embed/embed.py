from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chromadb
import json

def embed_text(transcript: str, title: str, description: str, tags: str) -> dict:
    # Use free HuggingFace embeddings
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )
    Settings.llm = None

    # Create document
    doc = Document(text=transcript)
    
    # Create index
    index = VectorStoreIndex.from_documents([doc])
    
    # Store in ChromaDB
    client = chromadb.PersistentClient(path="./chroma_db")
    
    rag_package = {
        "title": title,
        "description": description,
        "tags": tags.split(","),
        "transcript_length": len(transcript),
        "status": "ready"
    }
    
    return rag_package