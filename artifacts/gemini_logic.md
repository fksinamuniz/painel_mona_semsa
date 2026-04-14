# Lógica de Extração com Gemini AI

Este documento descreve a estratégia de **"Detecção de Estrutura sob Demanda"** utilizada para identificar seletores CSS automaticamente antes da raspagem de dados.

## 1. Etapas do Processo

### A. Simplificação do HTML (`simplifyHtml`)
Antes de enviar o conteúdo para o Gemini, o HTML bruto é limpo para remover ruídos e reduzir o consumo de tokens.
- **Remoção de:** `<script>`, `<style>`, `<svg>`.
- **Limpeza de:** Atributos inline (`style`, `onclick`) e `data-attributes`.

```typescript
// src/lib/gemini.ts
export function simplifyHtml(html: string): string {
  return html
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, "")
    .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, "")
    .replace(/<svg\b[^<]*(?:(?!<\/svg>)<[^<]*)*<\/svg>/gi, "")
    .replace(/\s(style|onclick|on\w+)="[^"]*"/gi, "")
    .replace(/\s(data-\w+)="[^"]*"/gi, "");
}
```

### B. Prompt Estruturado (`detectSiteStructure`)
O Gemini recebe o HTML simplificado e instruções do usuário, retornando estritamente um JSON com os seletores.

**Estrutura do Prompt:**
- **Instruções:** Campo livre do usuário (ex: "extraia nome e preço dos produtos").
- **HTML:** O código simplificado.
- **Formato esperado:**
  ```json
  {
    "parentSelector": "Seletor do container pai",
    "fields": {
      "field_name": "Seletor relativo"
    },
    "paginationSelector": "Seletor do botão 'Próximo'"
  }
  ```

### C. Orquestração do Fluxo (`runScraper`)
O sistema decide quando chamar a IA:
1. **Verificação:** Se o site não tem `config` ou `parentSelector` salvo.
2. **Descoberta:** Faz um scrape inicial para obter o HTML, limpa-o e chama o Gemini.
3. **Persistência:** Salva os seletores detectados no banco de dados (Prisma).
4. **Execução:** Realiza a raspagem real usando os seletores via Playwright.

## 2. Vantagens da Abordagem
- **Economia:** A IA só é consultada na configuração inicial ou quando as instruções mudam.
*   **Velocidade:** Raspagens recorrentes usam seletores CSS puros, sem latência de IA.
*   **Confiabilidade:** Evita alucinações de dados, pois a IA define a *forma* da extração, enquanto o Playwright lê os *dados reais*.
