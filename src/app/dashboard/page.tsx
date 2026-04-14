"use client";

import { useSession, signOut } from "next-auth/react";
import { useState, useEffect } from "react";
import { LogOut, Target, ArrowLeft, FileText } from "lucide-react";
import Link from "next/link";
import { useRouter } from "next/navigation";

export default function DashboardPage() {
  const router = useRouter();
  const { data: session, status } = useSession({
    required: true,
    onUnauthenticated() {
      router.push("/login");
    },
  });
  
  const [isMounted, setIsMounted] = useState(false);
  useEffect(() => {
    setIsMounted(true);
  }, []);

  if (status === "loading" || !isMounted) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <div className="animate-spin text-blue-600">Carregando...</div>
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col bg-slate-50 overflow-hidden">
      {/* Header */}
      <header className="w-full bg-white shadow-sm border-b border-slate-200 shrink-0 px-6 py-3 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <Link href="/" className="text-slate-500 hover:text-slate-700 bg-slate-100 hover:bg-slate-200 p-2 rounded-lg transition-colors" title="Voltar ao início">
            <ArrowLeft size={18} />
          </Link>
          <h1 className="text-lg font-bold tracking-tight text-slate-800 flex items-center gap-2">
            <Target className="text-blue-600" size={20} />
            Painel de Monitoramento
          </h1>
        </div>
        <div className="flex items-center gap-4">

          <a
            href="https://digisusgmp.saude.gov.br/"
            target="_blank" rel="noopener noreferrer"
            className="hidden md:flex items-center gap-2 text-sm px-4 py-1.5 bg-blue-50 text-blue-700 hover:bg-blue-100 hover:text-blue-800 font-semibold rounded-lg transition-colors border border-blue-200"
          >
            Acessar DigiSUS Gestor
          </a>
          <div className="text-sm font-medium text-slate-500 hidden sm:block">
            {session?.user?.name || "Usuário"}
          </div>
          <button
            onClick={() => signOut()}
            className="flex items-center gap-2 text-sm px-3 py-1.5 text-slate-600 hover:text-red-600 hover:bg-red-50 transition-colors rounded-lg font-medium"
          >
            <LogOut size={16} /> Sair
          </button>
        </div>
      </header>

      {/* Embedded External Project */}
      <main className="flex-1 w-full bg-white relative">
        <iframe 
          src="/monitoramento/index.html" 
          className="absolute inset-0 w-full h-full border-none"
          title="Projeto Monitoramento Externo"
        />
      </main>
    </div>
  );
}
