# Ragify — Autonomous Video-to-RAG Agent

**Turn any YouTube video into a queryable knowledge base in one command.**

```
python3 run_demo.py   # Jim Simons quant lecture → RAG
```

## Architecture

```
YouTube URL
    │
    ▼
[1] FETCH        yt-dlp → mp3 (64kbps)
    │
    ▼
[2] TRANSCRIBE   OpenAI Whisper-1 API
                 (auto-splits >24 MB audio via ffmpeg)
    │
    ▼
[3] CHUNK        Semantic boundary splitting
                 ~150 tokens/chunk, sentence-overlap
    │
    ▼
[4] EMBED        text-embedding-3-small (1536-dim)
                 Batched in groups of 32
    │
    ▼
[5] INDEX        ChromaDB persistent vector store
                 HNSW cosine similarity
    │
    ▼
[6] QUERY        Top-K retrieval → gpt-4o-mini
                 Cited answers with timestamps
```

## Quick Start

```bash
# 1. Install deps
pip install yt-dlp openai chromadb fastapi uvicorn tiktoken python-dotenv

# 2. Set your OpenAI key
export OPENAI_API_KEY=sk-...

# 3. Run the Jim Simons demo
python3 run_demo.py

# 4. Or start the API server
cd backend && python3 server.py
# → http://localhost:8765/docs
```

## API Endpoints

| Method | Endpoint  | Description                        |
|--------|-----------|------------------------------------|
| POST   | /ingest   | Start pipeline (SSE stream)        |
| POST   | /query    | RAG query → JSON answer            |
| GET    | /chunks   | List all indexed chunks            |
| GET    | /status   | Pipeline state                     |
| GET    | /health   | Health check                       |

### Ingest (SSE stream)
```bash
curl -N -X POST http://localhost:8765/ingest \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.youtube.com/watch?v=JGszY289a28"}'
```

### Query
```bash
curl -X POST http://localhost:8765/query \
  -H "Content-Type: application/json" \
  -d '{"question":"How did the Medallion Fund achieve its returns?"}'
```

## File Structure

```
ragify/
├── backend/
│   ├── pipeline.py    # Core RAG pipeline (fetch→embed→index→query)
│   └── server.py      # FastAPI server with SSE streaming
├── data/
│   └── chroma/        # Persistent ChromaDB vector store
├── run_demo.py        # CLI runner (Jim Simons lecture)
├── test_pipeline.py   # Logic verification (no API key needed)
└── README.md
```

## Costs (Jim Simons ~1hr lecture)

| Stage      | Model               | Approx Cost |
|------------|---------------------|-------------|
| Transcribe | whisper-1           | ~$0.36      |
| Embed      | text-embedding-3-small | ~$0.002  |
| Query (x5) | gpt-4o-mini         | ~$0.01      |
| **Total**  |                     | **~$0.37**  |

## Extending Ragify

- **More video sources**: swap `_fetch()` — yt-dlp supports 1000+ sites
- **Better chunking**: replace token-count with semantic similarity (cosine of adjacent segments)
- **Production index**: swap ChromaDB for Pinecone / Weaviate / pgvector
- **Streaming answers**: stream gpt-4o-mini tokens via SSE back to UI
- **Multi-video**: extend collection naming to support a library of indexed videos
