"use client";
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

type RAG = {
  id: string;
  title: string;
  creator: string;
  description: string;
  tags: string[];
  status: string;
};

export default function Marketplace() {
  const [rags, setRags] = useState<RAG[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchRags() {
      const { data } = await supabase
        .from("rags")
        .select("*")
        .order("created_at", { ascending: false });
      setRags(data || []);
      setLoading(false);
    }
    fetchRags();
  }, []);

  return (
    <main className="max-w-6xl mx-auto px-6 py-16">
      <div className="mb-12 text-center">
        <h1 className="text-4xl font-bold mb-4">RAG Marketplace</h1>
        <p className="text-white/50 text-lg">
          Browse RAG packages built from real expert content.
        </p>
      </div>

      {loading ? (
        <div className="text-center text-white/50">Loading RAGs...</div>
      ) : rags.length === 0 ? (
        <div className="text-center text-white/50">
          No RAGs yet — be the first to upload one!
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {rags.map((rag) => (
            <div
              key={rag.id}
              className="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition flex flex-col gap-4"
            >
              <div>
                <h2 className="font-semibold text-lg mb-1">{rag.title}</h2>
                <p className="text-white/40 text-sm">by {rag.creator}</p>
              </div>
              <p className="text-white/60 text-sm flex-1">{rag.description}</p>
              <div className="flex flex-wrap gap-2">
                {rag.tags.map((tag) => (
                  <span
                    key={tag}
                    className="bg-white/10 text-white/60 text-xs px-3 py-1 rounded-full"
                  >
                    {tag}
                  </span>
                ))}
              </div>
              <div className="flex items-center justify-between pt-2 border-t border-white/10">
                <span className="text-green-400 text-sm font-medium">
                  ✓ Ready
                </span>
                <button className="bg-white text-black text-sm px-4 py-2 rounded-full font-medium hover:bg-white/90 transition">
                  Download RAG
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </main>
  );
}