from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from transcribe.transcribe import transcribe_video
from embed.embed import embed_text
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/generate-rag")
async def generate_rag(
    title: str = Form(...),
    description: str = Form(...),
    youtube_url: str = Form(...),
    tags: str = Form(...),
):
    # Step 1 - Transcribe
    transcript = transcribe_video(youtube_url)
    
    # Step 2 - Embed
    rag_package = embed_text(transcript, title, description, tags)
    
    return {"success": True, "rag": rag_package}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)