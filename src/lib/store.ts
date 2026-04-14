import { create } from 'zustand'
import { persist } from 'zustand/middleware'

export type AvaliacaoAcao = {
  id: string
  // 1. Identificação
  objetivo: string
  contexto: string
  // 2. Metas e Medidas
  metaDescritiva: string
  metaNumerica: string
  polaridade: string
  unidadeMedida: string
  // 3. Cálculo e Referência
  numerador: string
  denominador: string
  fatorMultiplicador: string
  fonte: string
  // 4. Montoramento
  periodicidade: 'Mensal' | 'Quadrimestral'
  responsavel: string
  // Metadados
  dataRegistro: string
  status: 'Pendente' | 'Concluído'
}

type AcoesStore = {
  acoes: AvaliacaoAcao[]
  addAcao: (acao: AvaliacaoAcao) => void
  removeAcao: (id: string) => void
  updateAcao: (id: string, actionData: Partial<AvaliacaoAcao>) => void
  clearAll: () => void
}

export const useAcoesStore = create<AcoesStore>()(
  persist(
    (set) => ({
      acoes: [],
      addAcao: (acao) => set((state) => ({ acoes: [...state.acoes, acao] })),
      removeAcao: (id) =>
        set((state) => ({ acoes: state.acoes.filter((a) => a.id !== id) })),
      updateAcao: (id, update) =>
        set((state) => ({
          acoes: state.acoes.map((a) => (a.id === id ? { ...a, ...update } : a)),
        })),
      clearAll: () => set({ acoes: [] }),
    }),
    {
      name: 'acoes-storage', // name of the item in the storage (must be unique)
    }
  )
)
