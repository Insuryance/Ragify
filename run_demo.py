#!/usr/bin/env python3
"""
Ragify CLI — end-to-end demo runner
Usage:
    OPENAI_API_KEY=sk-... python3 run_demo.py

Ingests Jim Simons quant lecture, then runs 5 demo queries.
"""

import os, sys, time
from dataclasses import asdict

sys.path.insert(0, "/home/claude/ragify/backend")
from pipeline import RagifyPipeline

SIMONS_URL = "https://www.youtube.com/watch?v=JGszY289a28"

DEMO_QUERIES = [
    "What is Jim Simons' approach to quantitative trading and pattern recognition?",
    "How did the Medallion Fund achieve its extraordinary returns?",
    "What role does mathematics play in Simons' investment strategy?",
    "What does Simons say about hiring mathematicians and scientists over finance people?",
    "What were the early failures and pivots in Renaissance Technologies?",
]

CYAN  = "\033[96m"
GREEN = "\033[92m"
AMBER = "\033[93m"
RED   = "\033[91m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
RST   = "\033[0m"

def banner(text):
    print(f"\n{BOLD}{'─'*64}{RST}")
    print(f"{BOLD}  {text}{RST}")
    print(f"{BOLD}{'─'*64}{RST}\n")

def stage_line(stage, status, detail):
    icons = {
        "fetch":      "🎬", "transcribe": "🎙️",
        "chunk":      "✂️ ", "embed":      "🧠",
        "index":      "🗄️", "query":      "🔍",
        "pipeline":   "⚙️", "done":       "✅",
    }
    colors = {"running": AMBER, "done": GREEN, "error": RED}
    icon   = icons.get(stage, "▸")
    color  = colors.get(status, "")
    badge  = f"{color}[{status:8s}]{RST}"
    print(f"  {icon}  {badge}  {stage:<12s}  {DIM}{detail}{RST}")

def main():
    key = os.getenv("OPENAI_API_KEY", "")
    if not key:
        print(f"{RED}Error: OPENAI_API_KEY environment variable not set.{RST}")
        print("  export OPENAI_API_KEY=sk-...")
        sys.exit(1)

    banner("Ragify — Autonomous Video-to-RAG Agent")
    print(f"  {DIM}Video: {SIMONS_URL}{RST}\n")

    pipe = RagifyPipeline(openai_api_key=key)

    # ── Run pipeline ──────────────────────────────────────────────────────────
    print(f"{BOLD}▸ PIPELINE{RST}")
    t0 = time.time()
    chunks_data = []

    for evt in pipe.ingest(SIMONS_URL):
        stage_line(evt.stage, evt.status, evt.detail)
        if evt.stage == "chunk" and evt.status == "done":
            chunks_data = evt.data.get("chunks", [])

    elapsed = time.time() - t0
    print(f"\n  ✅  Pipeline complete in {elapsed:.1f}s")

    # ── Print chunk summary ───────────────────────────────────────────────────
    banner("Transcript Chunks")
    for c in chunks_data[:6]:
        start = pipe._fmt_time(c["start"])
        end   = pipe._fmt_time(c["end"])
        text  = c["text"][:110].replace("\n", " ")
        print(f"  {CYAN}#{c['id']:02d}{RST} [{start}→{end}] {DIM}{text}…{RST}")
    if len(chunks_data) > 6:
        print(f"  {DIM}… and {len(chunks_data)-6} more chunks{RST}")

    # ── Run demo queries ──────────────────────────────────────────────────────
    banner("RAG Queries")
    for i, q in enumerate(DEMO_QUERIES, 1):
        print(f"\n{BOLD}Q{i}: {q}{RST}")
        t_q = time.time()
        result = pipe.query(q)
        lat = int((time.time() - t_q) * 1000)

        print(f"\n{GREEN}Answer:{RST}")
        # Word-wrap at 72 chars
        words = result.answer.split()
        line = ""
        for w in words:
            if len(line) + len(w) + 1 > 72:
                print("  " + line)
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            print("  " + line)

        print(f"\n{DIM}Sources:{RST}")
        for c, s in zip(result.chunks[:3], result.scores[:3]):
            bar = "█" * int(s * 20)
            print(f"  {CYAN}#{c.id:02d}{RST} [{pipe._fmt_time(c.start)}] score={s:.3f} {DIM}{bar}{RST}")
        print(f"  {DIM}Latency: {lat}ms{RST}")
        print()

    banner("Done — Ragify RAG index ready for queries")
    print(f"  Collection: {pipe._video_id(SIMONS_URL)}")
    print(f"  Chunks:     {len(chunks_data)}")
    print(f"  Queries run:{len(DEMO_QUERIES)}")
    print(f"  Total time: {time.time()-t0:.1f}s\n")

if __name__ == "__main__":
    main()
