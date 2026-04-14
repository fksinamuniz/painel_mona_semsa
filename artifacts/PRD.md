# PRD: Web Scraping Inteligente com Gemini AI

## 1. Visão Geral
Um sistema de extração de dados web de alta performance que utiliza Inteligência Artificial (Google Gemini) para eliminar a necessidade de configuração manual de seletores CSS/XPath. O software automatiza o processo de "discovery" de dados e escala a extração através de containers Docker.

## 2. Funcionalidades Principais

### A. Dashboard Premium
- **Interface Glassmorphism**: UI moderna com foco em experiência do usuário e alta fidelidade visual.
- **Monitoramento em Tempo Real**: Indicadores de status (IDLE, RUNNING, COMPLETED, FAILED) para cada alvo.
- **Painel de Controle Central**: Acesso rápido a sites enfileirados, logs de IA e datasets.

### B. Motor de Scraping (Engine)
- **Playwright Integration**: Navegação via browser real (Chromium) para contornar sites dinâmicos e SPAs.
- **Multi-Value Extraction**: Capacidade de extrair listas completas (ex: todos os bônus ou módulos de uma vez).
- **Suporte a Proxy**: Configuração individual de proxy (Host, Porta, Usuário, Senha) para evitar bloqueios.

### C. Inteligência Artificial (Discovery)
- **Auto-Configuração via Gemini**: A IA analisa o HTML simplificado e descobre sozinha onde estão os dados solicitados.
- **Prompt Dinâmico**: O sistema reage a instruções em linguagem natural (ex: "extraia o preço e o link de checkout").
- **Reactive Re-discovery**: O sistema detecta mudanças nas instruções e força uma nova análise da IA automaticamente.

### D. Gestão de Dados
- **Importação em Massa (Bulk Import)**: Adição de dezenas de URLs de uma só vez através de uma lista de texto.
- **Visualizador de Datasets**: Modal interativo para visualizar resultados em JSON ou Grade, com suporte a download.
- **Persistência Local**: Banco de dados SQLite para armazenamento seguro de configurações e resultados.

### E. Transparência e Debug
- **Gemini AI Logs**: Histórico detalhado de como a IA interpretou o site e quais decisões tomou.
- **Persistent Logging**: Sistema de logs do sistema para rastreio de erros de rede ou execução.

## 3. Fluxo do Usuário
1. O usuário cadastra uma URL e uma instrução simples.
2. O Playwright acessa o site e simplifica o HTML.
3. O Gemini recebe o HTML e cria o "mapa" da extração.
4. O sistema executa a extração baseada no mapa da IA.
5. Os dados ficam disponíveis para visualização e exportação.
