# Walkthrough: Web Scraping Inteligente com Gemini AI

O projeto foi concluído com sucesso e está pronto para ser implantado no Portainer.

## Funcionalidades Implementadas
- **Autenticação de Segurança:** Fluxo de primeiro acesso para configurar administrador e login protegido por JWT.
- **Visualizador de Dados:** Modal integrado para visualizar e baixar os resultados extraídos em JSON.
- **Sites Enfileirados:** Gestão centralizada de todos os alvos de extração.
- **Gemini AI Logs:** Histórico persistente de todas as execuções e decisões da IA.
- **Gestão Completa:** Edição e exclusão de sites cadastrados com um clique.
- **Suporte a Proxy:** Configuração de Proxy individual por site.
- **Design Premium:** Interface 100% renovada com Glassmorphism, tipografia moderna e animações.
- **Portainer Ready:** Configuração completa com Docker e Docker Compose.
- **Estabilização:** Uso do Prisma 6 para garantir compatibilidade total com SQLite em produção.

## Demonstração da Interface
![Dashboard UI](/artifacts/test_scraper_ui.webp)

## Como Usar o Sistema

### 1. Configuração Inicial
1. Acesse o Dashboard.
2. No painel lateral, insira sua **Gemini API Key** (obtida no Google AI Studio).
3. Clique em **Salvar Chaves**.

### 2. Cadastrando um Site
1. Clique em **Adicionar Site**.
2. Preencha o nome, a URL e a instrução (ex: "extraia todos os preços de smartphones").
3. Clique em **Cadastrar e Iniciar**.

### 3. Execução e Inteligência
1. Na primeira execução, o sistema usará o Playwright para ler o site e enviará a estrutura para o Gemini.
2. O Gemini retornará os seletores CSS precisos.
3. Essas configurações são salvas para as próximas execuções.

## Implantação no Portainer
Para rodar no Portainer via **Stacks**:

1. Crie uma nova **Stack**.
2. Cole o conteúdo do arquivo [docker-compose.yml](file:///Users/andrealencar/GoogleAntigravity/WebScrapingAntigravity/docker-compose.yml).
3. Certifique-se de que o arquivo [Dockerfile](file:///Users/andrealencar/GoogleAntigravity/WebScrapingAntigravity/Dockerfile) está no mesmo diretório ou aponte para o repositório git.
4. Clique em **Deploy the stack**.

## Roteiro para Vídeo Demonstrativo

Para explicar o sistema de forma impactante, sugerimos este roteiro:

1.  **O Problema (0-30s)**: Mostre como é difícil configurar seletores manualmente e como sites mudam o tempo todo.
2.  **A Solução (30-60s)**: Apresente o Dashboard e o conceito de "Instruções IA". Mostre você digitando uma instrução em português.
3.  **A Mágica da IA (1-2 min)**: Clique em "Iniciar Extração". Mostre os logs do Gemini detectando os seletores automaticamente. Destaque que o sistema "enxerga" o site como um humano.
4.  **Escalabilidade (2-3 min)**: Demonstre a **Importação em Massa** de várias URLs e a visualização dos dados em grade/JSON.
5.  **Tecnologia (Final)**: Cite o uso de Next.js, Playwright e Gemini para um sistema robusto e "AI-Native".

---

## Documentação do Projeto
- [PRD.md](file:///artifacts/PRD.md): Documento de Requisitos do Produto.
- [Technical_Specs.md](file:///artifacts/Technical_Specs.md): Especificações Técnicas e Arquitetura.
