# Ragify
Upload a video. Generate a RAG. Sell it to AI Agents.
<div align="center">

# Ragify Everything!

### Upload a video. Generate a RAG. Sell it to AI Agents.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/Insuryance/Ragify)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support%20Ragify-yellow)](https://buymeacoffee.com/insuryance)
[![Contributors Welcome](https://img.shields.io/badge/Contributors-Welcome-brightgreen)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/Insuryance/Ragify?style=social)](https://github.com/Insuryance/Ragify/stargazers)

</div>

---

## 🤔 Well What is Ragify?

Ragify is an open source marketplace where creators or wanna be creators can turn their video content into **RAG packages** that AI agent builders can buy and plug directly into their agents.
Assume this to be like you create a tutorial and sell it to an AI Agent out there. Monetise your context about anything! 

Think of it like this:

- A trading expert records a video explaining their strategy
- Ragify turns that video into an AI-readable RAG package
- An AI agent builder buys that RAG and their agent now thinks like that trading expert

**Ragify = Coursera for RAG.**

---

## ✨ Features

-  **Upload any video** — YouTube link or Direct File Upload
-  **Auto transcription** — powered by OpenAI Whisper (free, local)
-  **Smart chunking** — powered by LlamaIndex
-  **Embeddings** — powered by HuggingFace free models
-  **Vector storage** — powered by ChromaDB
-  **Marketplace** — browse and download RAG packages
-  **Support creators** — via Buy Me a Coffee

---

## How it works
```
Creator uploads video
        ↓
Whisper transcribes audio to text
        ↓
LlamaIndex chunks the text smartly
        ↓
HuggingFace turns chunks into embeddings
        ↓
ChromaDB stores the vector database
        ↓
RAG package listed on Ragify marketplace
        ↓
AI agent builder buys and plugs it into their agent
```

---

## 🚀 Getting Started

### What you need before starting
- A Mac or Windows laptop
- Python 3.10 or higher ([download here](https://www.python.org/downloads/))
- Node.js 18 or higher ([download here](https://nodejs.org/))
- A free Supabase account ([sign up here](https://supabase.com))
- A free Vercel account ([sign up here](https://vercel.com))

### Step 1 — Clone the project
```bash
git clone https://github.com/Insuryance/Ragify.git
cd Ragify
```

### Step 2 — Install frontend dependencies
```bash
cd app
npm install
```

### Step 3 — Install backend dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 4 — Set up your environment variables
```bash
cp .env.local.example .env.local
```
Then open `.env.local` and fill in your Supabase keys.

### Step 5 — Run the project locally
```bash
# Terminal 1 - Frontend
cd app
npm run dev

# Terminal 2 - Backend
cd backend
python main.py
```

Visit `http://localhost:3000` to see Ragify running locally!

---

## 🏗️ Project Structure
```
Ragify/
├── app/                    # Next.js frontend
│   ├── components/         # Reusable UI components
│   │   ├── Navbar.jsx      # Top navigation bar
│   │   └── RAGCard.jsx     # RAG listing card
│   ├── marketplace/        # Marketplace page
│   │   └── page.jsx
│   ├── upload/             # Upload page
│   │   └── page.jsx
│   ├── page.jsx            # Homepage
│   └── layout.jsx          # App layout
├── backend/                # Python backend
│   ├── transcribe/         # Whisper transcription
│   ├── embed/              # HuggingFace embeddings
│   └── rag/                # RAG packaging
├── docs/                   # Documentation
├── public/                 # Static assets
├── CONTRIBUTING.md         # How to contribute
└── README.md               # You are here!
```

---

## 🤝 Contributing

Ragify is fully open source and we love contributions!

Whether you're fixing a bug, adding a feature, or improving docs —
**you are welcome here.**

Read our [Contributing Guide](CONTRIBUTING.md) to get started.

---

## 💛 Support Ragify

Ragify is free and open source forever.
If it helped you, consider buying the creator a coffee!

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Support%20Ragify-yellow)](https://buymeacoffee.com/Insuryance)

---

## 📄 License

MIT License — free to use, modify and distribute.

---

<div align="center">
Built with ❤️ by <a href="https://github.com/Insuryance">Insuryance</a> and the open source community
</div>