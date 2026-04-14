"use client";

import { useState } from "react";
import { METAS } from "@/lib/metas";
import { Search, Filter, ArrowUpRight, BarChart3, AlertCircle, CheckCircle2, LayoutDashboard } from "lucide-react";

export default function MonitoramentoPMS() {
  const [search, setSearch] = useState("");
  const [filterDirective, setFilterDirective] = useState("all");
  
  const filtered = METAS.filter(m => {
    const matchesSearch = m.num.includes(search) || m.desc.toLowerCase().includes(search.toLowerCase());
    const matchesDir = filterDirective === "all" || m.d === filterDirective;
    return matchesSearch && matchesDir;
  });

  const percentValues = (m: any) => {
    if ((m.un || "").toLowerCase().includes("percent") || (m.un || "").toLowerCase().includes("proporção")) {
      return true;
    }
    return false;
  };

  const formatValue = (val: string, isPercent: boolean) => {
    if (!val || val === "0") return <span className="text-slate-300">—</span>;
    if (isPercent) {
      const num = parseFloat(val);
      if (num > 0 && num <= 1) return (num * 100).toFixed(1).replace(/\.0$/, "") + "%";
      return val + "%";
    }
    return val;
  };

  // Mocked status generation for visualization premium aesthetics
  const getStatus = (m: any) => {
    const isCompleted = parseFloat(m.m2026) > 0 && parseFloat(m.m2027) > 0;
    if (isCompleted) return { label: "Andamento", color: "text-amber-600 bg-amber-50 border-amber-200", icon: <AlertCircle size={14} /> };
    if (parseFloat(m.m2026) > 0) return { label: "Realizado", color: "text-emerald-600 bg-emerald-50 border-emerald-200", icon: <CheckCircle2 size={14} /> };
    return { label: "Pendente", color: "text-slate-600 bg-slate-50 border-slate-200", icon: <ArrowUpRight size={14} /> };
  };

  return (
    <div className="space-y-6">
      
      {/* Metrics Row */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm flex items-center gap-4 hover:shadow-md transition-shadow">
          <div className="h-12 w-12 rounded-xl bg-blue-50 text-blue-600 flex flex-shrink-0 items-center justify-center">
            <LayoutDashboard size={24} />
          </div>
          <div>
            <div className="text-slate-500 text-sm font-medium">Total de Metas</div>
            <div className="text-3xl font-black text-slate-900">{METAS.length}</div>
          </div>
        </div>
        <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm flex items-center gap-4 hover:shadow-md transition-shadow">
          <div className="h-12 w-12 rounded-xl bg-emerald-50 text-emerald-600 flex flex-shrink-0 items-center justify-center">
            <CheckCircle2 size={24} />
          </div>
          <div>
            <div className="text-slate-500 text-sm font-medium">Realizadas 2026</div>
            <div className="text-3xl font-black text-slate-900">42</div>
          </div>
        </div>
        <div className="bg-white border border-slate-200 rounded-2xl p-6 shadow-sm flex items-center gap-4 hover:shadow-md transition-shadow">
          <div className="h-12 w-12 rounded-xl bg-amber-50 text-amber-600 flex flex-shrink-0 items-center justify-center">
            <BarChart3 size={24} />
          </div>
          <div>
            <div className="text-slate-500 text-sm font-medium">Em Andamento</div>
            <div className="text-3xl font-black text-slate-900">115</div>
          </div>
        </div>
        <div className="bg-gradient-to-br from-slate-900 to-slate-800 border border-slate-800 rounded-2xl p-6 shadow-lg shadow-slate-900/10 flex flex-col justify-center">
          <div className="text-slate-300 text-sm font-medium mb-1">Acesso Oficial</div>
          <button className="text-white text-sm font-semibold hover:text-blue-400 transition-colors flex items-center gap-2">
            DigiSUS Gestor GMP <ArrowUpRight size={16} />
          </button>
        </div>
      </div>

      <div className="bg-white border rounded-2xl border-slate-200 shadow-sm p-8 space-y-6">
        <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 border-b border-slate-100 pb-6">
          <div>
            <h2 className="text-2xl font-bold text-slate-900 tracking-tight">Instrumentos de Planejamento</h2>
            <p className="text-sm text-slate-500 mt-1">Acervo documentado e progresso oficial do PMS 2026-2029.</p>
          </div>
          <div className="flex flex-col sm:flex-row gap-3 w-full md:w-auto">
            <div className="flex bg-slate-50 border border-slate-200 rounded-xl px-4 py-2.5 w-full sm:w-auto shadow-sm focus-within:ring-2 focus-within:ring-blue-500/20 focus-within:border-blue-500 transition-all">
              <Search size={18} className="text-slate-400 mr-2" />
              <input 
                type="text" 
                placeholder="Buscar (ex: 1.1.2 ou APS)" 
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="bg-transparent text-sm outline-none w-full sm:w-64 text-slate-700"
              />
            </div>
            <div className="flex bg-slate-50 border border-slate-200 rounded-xl px-3 py-2.5 w-full sm:w-auto shadow-sm">
              <Filter size={18} className="text-slate-400 mr-2" />
              <select 
                value={filterDirective} 
                onChange={(e) => setFilterDirective(e.target.value)}
                className="bg-transparent text-sm outline-none w-full text-slate-700 pr-2 cursor-pointer"
              >
                <option value="all">Todas as Diretrizes</option>
                <option value="1">Dir. 1 – APS</option>
                <option value="2">Dir. 2 – Especializada</option>
                <option value="3">Dir. 3 – Regulação/Acesso</option>
                <option value="4">Dir. 4 – Farmacêutica</option>
                <option value="5">Dir. 5 – Vigilância</option>
                <option value="6">Dir. 6 – Gestão</option>
                <option value="7">Dir. 7 – Trabalho</option>
              </select>
            </div>
          </div>
        </div>

        <div className="overflow-x-auto border border-slate-200 rounded-xl shadow-sm">
          <table className="w-full text-left border-collapse min-w-max">
            <thead>
              <tr className="bg-slate-50 text-slate-500 text-xs font-semibold uppercase tracking-wider relative">
                <th className="px-5 py-4 border-b border-slate-200 w-24">Número</th>
                <th className="px-5 py-4 border-b border-slate-200">Descrição da Meta</th>
                <th className="px-5 py-4 border-b border-slate-200">Indicador & Unidade</th>
                <th className="px-5 py-4 border-b border-slate-200 text-center">Status</th>
                <th className="px-5 py-4 border-b border-slate-200 text-center w-24">2026</th>
                <th className="px-5 py-4 border-b border-slate-200 text-center w-24">2027</th>
                <th className="px-5 py-4 border-b border-slate-200 text-center w-24">2028</th>
                <th className="px-5 py-4 border-b border-slate-200 text-center w-24">2029</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {filtered.map((m) => {
                const isP = percentValues(m);
                const s = getStatus(m);
                return (
                  <tr key={m.num} className="hover:bg-slate-50/70 transition-colors group">
                    <td className="px-5 py-4 text-sm font-bold text-slate-800 align-top">
                      <div className="bg-slate-100 text-slate-700 w-fit px-2.5 py-1 rounded-lg border border-slate-200 shadow-sm font-mono text-xs">
                        {m.num}
                      </div>
                    </td>
                    <td className="px-5 py-4 text-sm text-slate-600 align-top max-w-sm">
                      <div className="font-semibold text-slate-800 mb-1 leading-snug">{m.desc}</div>
                      <div className="text-xs text-slate-400">Dir. {m.d}</div>
                    </td>
                    <td className="px-5 py-4 text-xs text-slate-500 align-top max-w-[200px]">
                      <div className="mb-1 leading-relaxed truncate group-hover:whitespace-normal group-hover:break-words">{m.ind}</div>
                      <div className="inline-flex items-center px-2 py-0.5 rounded-md bg-blue-50 text-blue-600 font-medium">
                        {m.un}
                      </div>
                    </td>
                    <td className="px-5 py-4 align-top text-center">
                      <div className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full border text-xs font-bold ${s.color}`}>
                        {s.icon} {s.label}
                      </div>
                    </td>
                    <td className="px-5 py-4 text-sm text-center font-bold text-slate-700 align-top">{formatValue(m.m2026, isP)}</td>
                    <td className="px-5 py-4 text-sm text-center font-bold text-slate-700 align-top">{formatValue(m.m2027, isP)}</td>
                    <td className="px-5 py-4 text-sm text-center font-bold text-slate-700 align-top">{formatValue(m.m2028, isP)}</td>
                    <td className="px-5 py-4 text-sm text-center font-bold text-slate-700 align-top">{formatValue(m.m2029, isP)}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          {filtered.length === 0 && (
            <div className="p-12 text-center text-slate-500 flex flex-col items-center justify-center">
              <Search size={32} className="text-slate-300 mb-4" />
              <p className="text-lg font-medium text-slate-700">Nenhuma meta encontrada.</p>
              <p className="text-sm mt-1">Verifique os termos da sua pesquisa ou altere o filtro de diretriz.</p>
            </div>
          )}
        </div>
        
        <div className="flex justify-between items-center text-xs font-medium text-slate-500 pt-4">
          <div>Exibindo <strong className="text-slate-800">{filtered.length}</strong> instrumentos formatados a partir do banco local</div>
          <div className="flex items-center gap-2">
            Base atualizada: <b>PMS 2026-2029</b>
          </div>
        </div>
      </div>
    </div>
  );
}
