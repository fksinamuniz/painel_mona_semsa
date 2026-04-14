# Technical Specs: Web Scraping Inteligente

## 1. Stack Tecnológica

### Core
- **Framework**: [Next.js 15 (App Router)](https://nextjs.org/)
- **Linguagem**: TypeScript (Strict Mode)
- **ORM**: [Prisma 6](https://www.prisma.io/)
- **Banco de Dados**: SQLite (Persistência em arquivo local)

### Engines & AI
- **Scraping**: [Playwright](https://playwright.dev/) (Chromium)
- **DOM Parsing**: [Cheerio](https://cheerio.js.org/)
- **Inteligência Artificial**: [Google Gemini Pro/Flash SDK](https://ai.google.dev/)

### UI/UX
- **Estilização**: TailwindCSS + Vanilla CSS (Custom Glassmorphism)
- **Ícones**: Lucide React
- **Animações**: Framer Motion

### Infraestrutura
- **Runtime**: Node.js 20+
- **Containerização**: Docker & Docker Compose
- **Implantação**: Otimizado para Stacks do Portainer

## 2. Arquitetura de Dados

### Modelo Prisma (Simplificado)
- **Site**: Armazena URL, Instruções, Configurações de Proxy e o "Mapa" JSON gerado pela IA.
- **Extraction**: Armazena os resultados brutas das raspagens vinculadas a um site.
- **Log**: Histórico de eventos do sistema e interações com a API Gemini.
- **AppConfig**: Armazenamento seguro de chaves de API (Gemini API Key).

## 3. Otimizações de Performance
- **Simplified DOM**: Antes de enviar o HTML para o Gemini, o sistema remove scripts, estilos, SVGs e atributos de telemetria para reduzir o consumo de tokens e aumentar a precisão.
- **Cached Selectors**: O sistema armazena os seletores CSS descobertos. Uma nova análise de IA só ocorre se as instruções forem alteradas ou se a extração falhar.
- **Zero-Config Deployment**: O banco SQLite é inicializado automaticamente via Docker Volumes, garantindo que o sistema esteja pronto para uso imediato após o deploy.

## 4. Segurança
- **Token Fallback**: Mecanismo de fallback em memória para autenticação.
- **Proxy Masking**: Suporte a proxies autenticados para evitar IP banning do servidor de scraping.
- **Hashed Passwords**: Segurança de credenciais de administrador via Bcrypt.
