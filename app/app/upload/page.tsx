export default function Upload() {
  return (
    <main className="max-w-2xl mx-auto px-6 py-16">

      {/* Header */}
      <div className="mb-10 text-center">
        <h1 className="text-4xl font-bold mb-4">Sell your RAG</h1>
        <p className="text-white/50">Turn your video content into a RAG package and list it on the marketplace.</p>
      </div>

      {/* Form */}
      <div className="bg-white/5 border border-white/10 rounded-2xl p-8 flex flex-col gap-6">

        {/* RAG Title */}
        <div className="flex flex-col gap-2">
          <label className="text-sm text-white/70">RAG Title</label>
          <input
            type="text"
            placeholder="e.g. Trading Strategy Masterclass"
            className="bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-white placeholder:text-white/30 focus:outline-none focus:border-white/50 transition"
          />
        </div>

        {/* Description */}
        <div className="flex flex-col gap-2">
          <label className="text-sm text-white/70">Description</label>
          <textarea
            placeholder="What does your RAG cover? Who is it for?"
            rows={4}
            className="bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-white placeholder:text-white/30 focus:outline-none focus:border-white/50 transition resize-none"
          />
        </div>

        {/* YouTube Link */}
        <div className="flex flex-col gap-2">
          <label className="text-sm text-white/70">YouTube Link</label>
          <input
            type="url"
            placeholder="https://youtube.com/watch?v=..."
            className="bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-white placeholder:text-white/30 focus:outline-none focus:border-white/50 transition"
          />
        </div>

        {/* Tags */}
        <div className="flex flex-col gap-2">
          <label className="text-sm text-white/70">Tags (comma separated)</label>
          <input
            type="text"
            placeholder="e.g. Trading, Finance, Strategy"
            className="bg-white/10 border border-white/20 rounded-xl px-4 py-3 text-white placeholder:text-white/30 focus:outline-none focus:border-white/50 transition"
          />
        </div>

        {/* Submit */}
        <button className="bg-white text-black px-8 py-3 rounded-full font-semibold hover:bg-white/90 transition text-sm mt-2">
          Generate my RAG →
        </button>

        {/* Note */}
        <p className="text-white/30 text-xs text-center">
          This is free and open source. If Ragify helped you, consider{" "}
          <a href="https://buymeacoffee.com" target="_blank" className="underline hover:text-white/60 transition">
            buying us a coffee ☕
          </a>
        </p>

      </div>
    </main>
  );
}