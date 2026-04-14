"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import {
  ArrowRight,
  BarChart3,
  BookMarked,
  CalendarDays,
  CheckCircle2,
  ClipboardCheck,
  Database,
  FileText,
  LineChart,
  Network,
  ShieldCheck,
  Users,
  History
} from "lucide-react";

export default function Planejamento_SUS() {
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        duration: 0.5
      }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { opacity: 1, y: 0, transition: { duration: 0.5 } }
  };

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800 font-sans selection:bg-blue-100 selection:text-blue-900">

      {/* 1. Hero Section */}
      <section className="relative pt-24 pb-32 overflow-hidden bg-white">
        <div className="absolute inset-0 border-b border-slate-200/60 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-blue-50/50 via-white to-white"></div>
        <div className="max-w-7xl mx-auto px-6 relative z-10">
          <motion.div
            className="grid lg:grid-cols-2 gap-12 items-center"
            initial="hidden"
            animate="visible"
            variants={containerVariants}
          >
            <div className="max-w-2xl">
              <motion.div variants={itemVariants} className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-100 text-blue-700 text-sm font-semibold mb-6">
                <ShieldCheck size={16} /> Monitoramento Oficial do SUS
              </motion.div>
              <motion.h1 variants={itemVariants} className="text-4xl md:text-5xl lg:text-6xl font-black text-slate-900 leading-[1.1] tracking-tight mb-6">
                Transparência e Eficiência no <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-emerald-500">Ciclo de Planejamento</span> do SUS
              </motion.h1>
              <motion.p variants={itemVariants} className="text-lg md:text-xl text-slate-600 mb-8 leading-relaxed">
                Acompanhe o planejamento, as metas e a aplicação dos recursos públicos em saúde. Uma plataforma para gestores e cidadãos monitorarem os instrumentos oficiais: <strong>PMS, PAS, RDQA e RAG</strong> de forma integrada.
              </motion.p>
              <motion.div variants={itemVariants} className="flex flex-col sm:flex-row flex-wrap gap-4">
                <Link
                  href="/dashboard"
                  className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl bg-slate-900 text-white font-semibold hover:bg-slate-800 transition-all shadow-xl shadow-slate-900/10 active:scale-[0.98] group"
                >
                  Painel de Monitoramento
                  <ArrowRight size={18} className="group-hover:translate-x-1 transition-transform" />
                </Link>
                <Link
                  href="https://paineis-ms.vercel.app/"
                  target="_blank" rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl bg-blue-600 border-2 border-blue-600 text-white font-semibold hover:bg-blue-700 hover:border-blue-700 transition-all active:scale-[0.98] shadow-lg shadow-blue-500/20"
                >
                  <LineChart size={18} /> Explorar Painéis SUS
                </Link>
                <Link
                  href="https://digisusgmp.saude.gov.br/"
                  target="_blank" rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl bg-white border-2 border-slate-200 text-slate-700 font-semibold hover:border-slate-300 hover:bg-slate-50 transition-all active:scale-[0.98]"
                >
                  Acessar DigiSUS Gestor
                </Link>
                <Link
                  href="https://instrumentos-semsa.vercel.app/"
                  target="_blank" rel="noopener noreferrer"
                  className="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-xl bg-indigo-600 border-2 border-indigo-600 text-white font-semibold hover:bg-indigo-700 hover:border-indigo-700 transition-all active:scale-[0.98] shadow-lg shadow-indigo-500/20"
                >
                  <BarChart3 size={18} /> Painel RAG V. 01
                </Link>
              </motion.div>
            </div>

            {/* Hero Visual Concept */}
            <motion.div variants={itemVariants} className="relative hidden lg:block h-[500px]">
              <div className="absolute inset-0 bg-blue-500/5 rounded-full blur-3xl"></div>
              <div className="relative h-full flex items-center justify-center">
                <div className="relative w-full max-w-md aspect-square bg-white border border-slate-200/60 rounded-3xl shadow-2xl overflow-hidden shadow-blue-500/5">
                  <div className="absolute inset-0 bg-gradient-to-br from-blue-50/50 to-emerald-50/20"></div>
                  <div className="relative p-8 h-full flex flex-col justify-center gap-6">
                    <div className="space-y-4 w-full">
                      {[
                        { 
                          name: "Plano Municipal de Saúde", 
                          icon: <BookMarked size={18} className="text-blue-500" />,
                          link: "file:///C:/Users/frank.muniz/Nextcloud/PLANEJAMENTO/INSTRUMENTOS DE GESTÃO DO SUS/INSTRUMNETOS SUS - 2026/Plano Municipal de Saúde 2026 a 2029/PLANO DE SAÚDE ATUAL 2026- 2029 final.docx"
                        },
                        { 
                          name: "Programação Anual (PAS)", 
                          icon: <CalendarDays size={18} className="text-indigo-500" />,
                          link: "#"
                        },
                        { 
                          name: "Relatório de Gestão (RAG)", 
                          icon: <FileText size={18} className="text-emerald-500" />,
                          link: "#"
                        }
                      ].map((doc, i) => (
                        <motion.a 
                          key={i}
                          href={doc.link}
                          target="_blank"
                          rel="noopener noreferrer"
                          initial={{ opacity: 0, x: -20 }}
                          animate={{ opacity: 1, x: 0 }}
                          transition={{ delay: 0.5 + (i * 0.2) }}
                          className="flex items-center gap-4 p-4 bg-white rounded-xl shadow-sm border border-slate-200 hover:border-blue-400 hover:shadow-md transition-all group cursor-pointer"
                        >
                          <div className="w-10 h-10 rounded-lg bg-slate-50 flex items-center justify-center group-hover:bg-blue-50 transition-colors">
                            {doc.icon}
                          </div>
                          <div className="flex-1">
                            <div className="text-sm font-bold text-slate-800">{doc.name}</div>
                            <div className="text-xs text-slate-400 mt-0.5">Abrir documento oficial</div>
                          </div>
                          <div className="text-slate-300 group-hover:text-blue-500 transition-colors">
                            <ArrowRight size={16} />
                          </div>
                        </motion.a>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </motion.div>
          </motion.div>
        </div>
      </section>

      {/* 2. Seção de Serviços: O Ciclo de Planejamento */}
      <section className="py-24 bg-slate-50">
        <div className="max-w-7xl mx-auto px-6">
          <div className="text-center max-w-3xl mx-auto mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-slate-900 mb-6">O Ciclo de Planejamento do SUS</h2>
            <p className="text-lg text-slate-600">
              O planejamento no âmbito do SUS é de responsabilidade de cada ente federado, desenvolvido de forma contínua, articulada e integrada do nível local ao federal. Conheça os pilares deste ciclo:
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                title: "Plano de Saúde (PS / PMS)",
                icon: <BookMarked className="text-blue-500" size={32} />,
                accent: "border-blue-500",
                bg: "bg-blue-50",
                desc: "Instrumento central de planejamento para o período de 4 anos. Define Diretrizes, Objetivos, Metas e Indicadores (DOMI) com base nas necessidades reais e no perfil epidemiológico da população."
              },
              {
                title: "Programação Anual (PAS)",
                icon: <CalendarDays className="text-indigo-500" size={32} />,
                accent: "border-indigo-500",
                bg: "bg-indigo-50",
                desc: "A ferramenta que operacionaliza o Plano de Saúde a cada ano. Anualiza as metas e prevê a alocação dos recursos orçamentários necessários para a execução das ações."
              },
              {
                title: "Relatórios (RDQA)",
                icon: <LineChart className="text-emerald-500" size={32} />,
                accent: "border-emerald-500",
                bg: "bg-emerald-50",
                desc: "O termômetro da gestão. Apresentado em maio, setembro e fevereiro, permite o monitoramento da execução física e financeira das ações programadas na PAS."
              },
              {
                title: "Relatório Anual (RAG)",
                icon: <ClipboardCheck className="text-slate-700" size={32} />,
                accent: "border-slate-700",
                bg: "bg-slate-100",
                desc: "A prestação de contas definitiva do exercício. Apresenta os resultados anuais alcançados, a análise da execução orçamentária e orienta redirecionamentos."
              }
            ].map((card, idx) => (
              <motion.div
                key={idx}
                whileHover={{ y: -8 }}
                className={`bg-white rounded-2xl p-8 border-t-4 shadow-sm border-slate-200 border-t-transparent hover:${card.accent} transition-all duration-300 hover:shadow-xl group`}
                style={{ borderTopColor: idx === 0 ? '#3b82f6' : idx === 1 ? '#6366f1' : idx === 2 ? '#10b981' : '#334155' }}
              >
                <div className={`w-16 h-16 rounded-xl ${card.bg} flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300`}>
                  {card.icon}
                </div>
                <h3 className="text-xl font-bold text-slate-900 mb-4">{card.title}</h3>
                <p className="text-slate-600 leading-relaxed text-sm">
                  {card.desc}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* 3. Seção de Tecnologia: DigiSUS */}
      <section className="py-24 bg-white border-y border-slate-200/50 relative overflow-hidden">
        <div className="absolute top-0 right-0 -mt-24 -mr-24 w-96 h-96 bg-blue-50 rounded-full blur-3xl opacity-50"></div>
        <div className="max-w-7xl mx-auto px-6 relative z-10">
          <div className="flex flex-col lg:flex-row items-center gap-16">
            <div className="lg:w-1/2">
              <h2 className="text-3xl md:text-4xl font-bold text-slate-900 mb-6">Gestão Inteligente com o DigiSUS <br /><span className="text-blue-600 text-2xl font-semibold">Módulo Planejamento (DGMP)</span></h2>
              <p className="text-lg text-slate-600 mb-8">
                O monitoramento oficial dos instrumentos de saúde ocorre no ambiente digital do DGMP. O sistema consolida as informações da saúde e promove a transparência do uso de recursos públicos.
              </p>
              <ul className="space-y-6">
                {[
                  { title: "Integração de Dados", desc: "Conectado às principais bases nacionais, como SIOPS (orçamento), SCNES (estabelecimentos), SISAB (atenção básica), SIM e SINASC.", icon: <Database className="text-blue-500" /> },
                  { title: "Pactuação Interfederativa", desc: "Acompanhamento transparente das metas e indicadores pactuados entre municípios, estados e a União.", icon: <Network className="text-blue-500" /> },
                  { title: "Série Histórica", desc: "Disponibilização de histórico de indicadores para qualificar a avaliação dos resultados alcançados.", icon: <History className="text-blue-500" /> }
                ].map((item, idx) => (
                  <li key={idx} className="flex gap-4">
                    <div className="shrink-0 w-12 h-12 rounded-full bg-blue-50 flex items-center justify-center border border-blue-100">
                      {item.icon}
                    </div>
                    <div>
                      <h4 className="text-lg font-bold text-slate-900 mb-1">{item.title}</h4>
                      <p className="text-slate-600">{item.desc}</p>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
            <div className="lg:w-1/2 w-full">
              <div className="bg-slate-900 rounded-3xl p-2 shadow-2xl relative">
                <div className="absolute -inset-1 rounded-3xl bg-gradient-to-tr from-blue-600 to-emerald-400 opacity-20 blur"></div>
                <div className="bg-white rounded-2xl overflow-hidden aspect-[4/3] flex items-center justify-center relative">
                  {/* Mockup UI for DigiSUS interface */}
                  <div className="absolute inset-0 bg-slate-50 flex flex-col">
                    <div className="h-12 border-b border-slate-200 bg-white flex items-center px-4 gap-4">
                      <div className="flex gap-1.5">
                        <div className="w-3 h-3 rounded-full bg-red-400"></div>
                        <div className="w-3 h-3 rounded-full bg-amber-400"></div>
                        <div className="w-3 h-3 rounded-full bg-emerald-400"></div>
                      </div>
                      <div className="h-6 w-full max-w-xs bg-slate-100 rounded mx-auto"></div>
                    </div>
                    <div className="p-6 flex-1 flex flex-col gap-4">
                      <div className="h-8 w-48 bg-slate-200 rounded"></div>
                      <div className="grid grid-cols-3 gap-4 mb-4">
                        <div className="h-24 bg-blue-50 rounded-xl border border-blue-100"></div>
                        <div className="h-24 bg-emerald-50 rounded-xl border border-emerald-100"></div>
                        <div className="h-24 bg-indigo-50 rounded-xl border border-indigo-100"></div>
                      </div>
                      <div className="flex-1 bg-white rounded-xl border border-slate-200"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* 4. Seção de Participação: Controle Social */}
      <section className="py-24 bg-slate-900 text-white relative overflow-hidden">
        <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/cubes.png')] opacity-5"></div>
        <div className="max-w-7xl mx-auto px-6 relative z-10 text-center">
          <div className="w-16 h-16 bg-blue-500/20 text-blue-400 rounded-2xl flex items-center justify-center mx-auto mb-8 border border-blue-500/30">
            <Users size={32} />
          </div>
          <h2 className="text-3xl md:text-4xl font-bold mb-6">A Força do Controle Social na Saúde</h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto mb-16 leading-relaxed">
            A transparência e a visibilidade das políticas de saúde são asseguradas mediante o incentivo à participação popular. Os Conselhos de Saúde exercem um papel deliberativo fundamental em todas as etapas.
          </p>

          <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto mb-16 text-left">
            <div className="bg-slate-800/50 p-8 rounded-2xl border border-slate-700 backdrop-blur-sm">
              <FileText className="text-emerald-400 mb-4" size={28} />
              <h3 className="text-xl font-bold mb-3">Formulações do Plano</h3>
              <p className="text-slate-400">
                Aprovação das diretrizes para a formulação do Plano de Saúde representam a voz da sociedade na alocação de recursos.
              </p>
            </div>
            <div className="bg-slate-800/50 p-8 rounded-2xl border border-slate-700 backdrop-blur-sm">
              <CheckCircle2 className="text-blue-400 mb-4" size={28} />
              <h3 className="text-xl font-bold mb-3">Avaliação e Parecer</h3>
              <p className="text-slate-400">
                Avaliação quadrimestral do RDQA e emissão de parecer conclusivo anual sobre o RAG diretamente pelo sistema.
              </p>
            </div>
          </div>

          <button className="px-8 py-4 rounded-xl bg-blue-600 text-white font-semibold hover:bg-blue-500 transition-colors shadow-lg shadow-blue-600/20">
            Consulte as Resoluções e Pareceres do Conselho
          </button>
        </div>
      </section>

      {/* 5. Rodapé (Footer) */}
      <footer className="bg-slate-50 border-t border-slate-200 pt-16 pb-8 text-slate-600">
        <div className="max-w-7xl mx-auto px-6">
          <div className="grid md:grid-cols-3 gap-12 mb-12">
            <div>
              <h4 className="font-bold text-slate-900 mb-6 uppercase tracking-wider text-sm">Links Úteis | Base Legal</h4>
              <ul className="space-y-3 text-sm">
                <li><a href="#" className="hover:text-blue-600 transition-colors">Lei 8.080/1990</a></li>
                <li><a href="#" className="hover:text-blue-600 transition-colors">Lei Complementar 141/2012</a></li>
                <li><a href="#" className="hover:text-blue-600 transition-colors">Decreto 7.508/2011</a></li>
                <li><a href="#" className="hover:text-blue-600 transition-colors">Portaria de Consolidação nº 1/2017</a></li>
              </ul>
            </div>

            <div className="flex flex-col items-start gap-4">
              <h4 className="font-bold text-slate-900 mb-2 uppercase tracking-wider text-sm">Institucional</h4>
              <div className="flex flex-wrap gap-4">
                <div className="h-12 px-4 bg-white border border-slate-200 rounded-lg flex items-center justify-center font-bold text-slate-800">Ministério da Saúde</div>
                <div className="h-12 px-4 bg-white border border-slate-200 rounded-lg flex items-center justify-center font-bold text-slate-800 text-blue-600">SUS</div>
                <div className="h-12 px-4 bg-white border border-slate-200 rounded-lg flex items-center justify-center font-bold text-slate-800">Governo Federal</div>
              </div>
            </div>

            <div>
              <h4 className="font-bold text-slate-900 mb-6 uppercase tracking-wider text-sm">Contato</h4>
              <div className="bg-blue-50 border border-blue-100 rounded-xl p-6">
                <div className="text-2xl font-black text-blue-600 mb-1">Disque 136</div>
                <div className="text-sm text-blue-800 font-medium font-semibold">Ouvidoria do SUS</div>
                <p className="text-xs text-blue-600/80 mt-2">Dúvidas, reclamações, sugestões e elogios.</p>
              </div>
            </div>
          </div>

          <div className="pt-8 border-t border-slate-200 text-sm flex flex-col md:flex-row justify-between items-center gap-4">
            <p>2026 Sistema Único de Saúde - Módulo Gestão.</p>
            <p className="text-slate-400">Este é um projeto em desenvolvimento.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
