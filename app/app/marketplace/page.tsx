const rags = [
  {
    id: 1,
    title: "Trading Strategy Masterclass",
    creator: "TradingGuru",
    description: "Complete RAG package from 10 hours of trading strategy content. Covers RSI, MACD, price action and more.",
    tags: ["Trading", "Finance", "Strategy"],
    price: "Free",
  },
  {
    id: 2,
    title: "Python for Beginners",
    creator: "CodeWithMe",
    description: "Beginner to intermediate Python RAG. Covers variables, functions, OOP, and projects.",
    tags: ["Python", "Coding", "Beginner"],
    price: "Free",
  },
  {
    id: 3,
    title: "Digital Marketing 101",
    creator: "MarketingPro",
    description: "Full RAG on SEO, paid ads, email marketing and social media strategy.",
    tags: ["Marketing", "SEO", "Growth"],
    price: "Free",
  },
];

export default function Marketplace() {
  return (
    <main className="max-w-6xl mx-auto px-6 py-16">

      {/* Header */}
      <div className="mb-12 text-center">
        <h1 className="text-4xl font-bold mb-4">RAG Marketplace</h1>
        <p className="text-white/50 text-lg">Browse RAG packages built from real expert content. Plug them into your AI agent instantly.</p>
      </div>

      {/* Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {rags.map((rag) => (
          <div key={rag.id} className="bg-white/5 border border-white/10 rounded-2xl p-6 hover:bg-white/10 transition flex flex-col gap-4">
            
            {/* Title */}
            <div>
              <h2 className="font-semibold text-lg mb-1">{rag.title}</h2>
              <p className="text-white/40 text-sm">by {rag.creator}</p>
            </div>

            {/* Description */}
            <p className="text-white/60 text-sm flex-1">{rag.description}</p>

            {/* Tags */}
            <div className="flex flex-wrap gap-2">
              {rag.tags.map((tag) => (
                <span key={tag} className="bg-white/10 text-white/60 text-xs px-3 py-1 rounded-full">
                  {tag}
                </span>
              ))}
            </div>

            {/* Footer */}
            <div className="flex items-center justify-between pt-2 border-t border-white/10">
              <span className="text-white font-semibold">{rag.price}</span>
              <button className="bg-white text-black text-sm px-4 py-2 rounded-full font-medium hover:bg-white/90 transition">
                Download RAG
              </button>
            </div>

          </div>
        ))}
      </div>
    </main>
  );
}