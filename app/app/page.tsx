import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center min-h-[90vh] px-6 text-center">

      {/* Hero Badge */}
      <div className="mb-6 inline-flex items-center gap-2 bg-white/10 border border-white/20 rounded-full px-4 py-1.5 text-sm text-white/70">
        🚀 The RAG marketplace for AI agents
      </div>

      {/* Hero Title */}
      <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6 bg-gradient-to-b from-white to-white/50 bg-clip-text text-transparent">
        Upload a video.<br />
        Sell your knowledge.<br />
        Power AI agents.
      </h1>

      {/* Hero Subtitle */}
      <p className="text-lg text-white/50 max-w-xl mb-10">
        Ragify turns any video into a RAG package that AI agent builders can plug directly into their agents. Think Coursera — but for RAG.
      </p>

      {/* CTA Buttons */}
      <div className="flex flex-col sm:flex-row gap-4">
        <Link
          href="/marketplace"
          className="bg-white text-black px-8 py-3 rounded-full font-semibold hover:bg-white/90 transition text-sm"
        >
          Browse Marketplace
        </Link>
        <Link
          href="/upload"
          className="border border-white/20 text-white px-8 py-3 rounded-full font-semibold hover:bg-white/10 transition text-sm"
        >
          Sell your RAG →
        </Link>
      </div>

      {/* How it works */}
      <div className="mt-24 grid grid-cols-1 sm:grid-cols-3 gap-6 max-w-3xl w-full text-left">
        {[
          { step: "01", title: "Upload your video", desc: "Share a YouTube link or upload a video file of your expertise." },
          { step: "02", title: "We generate your RAG", desc: "Ragify transcribes, chunks, embeds and packages your knowledge automatically." },
          { step: "03", title: "Sell to AI agents", desc: "List your RAG on the marketplace. Builders plug it into their AI agents instantly." },
        ].map((item) => (
          <div key={item.step} className="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition">
            <div className="text-white/30 text-sm font-mono mb-2">{item.step}</div>
            <div className="font-semibold mb-2">{item.title}</div>
            <div className="text-white/50 text-sm">{item.desc}</div>
          </div>
        ))}
      </div>

    </main>
  );
}