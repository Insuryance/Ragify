import type { Metadata } from "next";
import { Geist } from "next/font/google";
import "./globals.css";
import Link from "next/link";

const geist = Geist({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Ragify — RAG Marketplace for AI Agents",
  description: "Upload a video. Generate a RAG. Sell it to AI Agents.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={`${geist.className} bg-black text-white min-h-screen`}>
        <nav className="border-b border-white/10 px-6 py-4 flex items-center justify-between sticky top-0 bg-black/80 backdrop-blur-md z-50">
          <Link href="/" className="text-xl font-bold text-white flex items-center gap-2">
            🧠 Ragify
          </Link>
          <div className="flex items-center gap-6">
            <Link href="/marketplace" className="text-sm text-white/70 hover:text-white transition">
              Marketplace
            </Link>
            <Link href="/upload" className="text-sm bg-white text-black px-4 py-2 rounded-full font-medium hover:bg-white/90 transition">
              Sell your RAG
            </Link>
          </div>
        </nav>
        {children}
      </body>
    </html>
  );
}