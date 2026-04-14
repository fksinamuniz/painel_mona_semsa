# Configurable Web Scraping Tool

The goal is to create a web-based scraping tool that allows users to configure the target site, the content to extract (CSS selectors/XPath), and proxy settings through a simple, premium UI.

## Technology Recommendations

I recommend the following stack for a robust, modern, and user-friendly experience:

### 1. Frontend & Backend: **Next.js (App Router)**
- **Why?** Full-stack capability. We'll use it for the Premium Dashboard and the Scraping/AI API routes.

### 2. Scraping Engine: **Playwright**
- **Why?** Robust handling of dynamic content. We'll use it to take "snapshots" of HTML to send to Gemini.

### 3. AI Integration: **Gemini API (Google AI SDK)**
- **Why?** It will analyze the HTML structure automatically to detect relevant content (names, prices, etc.), removing the need for manual selector configuration.

### 4. Database & Auth: **Prisma + SQLite**
- **Why?** To persist site registrations, API keys, and configurations locally.

### 5. Containerization: **Docker & Portainer**
- **Why?** To run the system on Portainer, we'll create a Docker image. Next.js will run inside a container, and we'll use a volume to persist the SQLite database.

## Proposed Architecture

- **Dashboard**: A premium interface featuring:
    - **Site Registration**: CRUD for target sites.
    - **Config Section**: Secure storage for Gemini API keys and Proxy settings.
    - **Progress Indicators**: Real-time status for active scraping tasks.
- **AI-Powered Discovery Workflow**:
    1. **Playwright** loads the site and takes a "structural snapshot".
    2. **DOM Simplifier**: A utility to strip noise (scripts, styles, SVG) and keep only structural tags and relevant attributes.
    3. **Gemini API Call**: Sends simplified HTML + goal (e.g., "extraia todos os produtos") to Gemini.
    4. **Smart Configuration**: Gemini returns a JSON mapping of CSS selectors and pagination logic.
    5. **Persistence/Caching**: The selectors are saved in the database for future runs, ensuring efficiency and cost-saving.
- **Deployment**:
    - **Dockerized**: A `Dockerfile` and `docker-compose.yml` will be provided.
    - **Portainer Compatible**: You can deploy it as a "Stack" in Portainer.
    - **Persistence**: The SQLite database and any downloaded content will be stored in a Docker Volume.

## Verification Plan

### Automated Tests
- Script to verify scraping of a mock HTML page.
- Test for proxy connectivity.

### Manual Verification
- Testing with several well-known sites (with their permission/terms of service in mind).
- Verifying the UI responsiveness and "wowed" aesthetics.

# Data Visualization Implementation

## Goal
Make the extracted data easily accessible and professionally presented.

## Proposed Changes

### [Component] SiteCard.tsx
- Move the result view button to be more prominent.
- Add a "View Latest Dataset" text instead of just an icon.

### [Page] /extractions/page.tsx
- Implement a server component to fetch all extractions.
- Create a professional table or grid view for datasets.
- Add capability to delete or download datasets directly from this list.

### [Component] ViewResultsModal.tsx
- Add a table view option (Grid view) for easier readability of extracted data, in addition to the raw JSON view.

# Sidebar Modules Implementation

## Goal
Implement fully functional pages for all sidebar menu items to provide a comprehensive management experience.

## Proposed Changes

### [Database] schema.prisma
- Add a `Log` model to store system messages, Gemini API calls, and errors.
- Fields: `id`, `type` (INFO, ERROR, GEMINI), `message`, `siteId` (optional), `createdAt`.

### [Page] /sites/page.tsx
- Implement a detailed list of all sites.
- Show status, last run time, and quick actions (Run, Delete).
- Highlight "Enqueued" status if a global queue system is added in the future.

### [Page] /ai-logs/page.tsx
- Create a professional centralized log viewer.
- Filter logs by type or site.
- Auto-refresh or "Live" mode if possible.

### [Actions] logActions.ts [NEW]
- Create server actions to save logs to the database and fetch them.

### [Refactor] scrape.ts
- Update the `runScraper` action to save logs to the database during execution.

# Bulk Site Import

## Goal
Enable users to add multiple sites at once to increase productivity.

## Proposed Changes

### [Actions] scrape.ts
- Create a `bulkAddSites` server action.
- This action will take a list of URLs and create multiple `Site` entries in one go.

### [Component] BulkAddModal.tsx [NEW]
- Create a new modal component with a large text area.
- Each line in the text area will be treated as a separate URL.
- Show a simple preview of how many sites will be added.

### [Page] Dashboard & Sites
- Add a "Bulk Import" button next to the standard "Add Site" button.
