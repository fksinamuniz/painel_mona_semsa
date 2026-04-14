# SUS Landing Page Plan

## Overview
Create a responsive, modern landing page for the "Ciclo de Planejamento do SUS" with a dark/light mode friendly professional UI, following the exact wireframe structure provided by the user.

## Project Type
WEB (Next.js App Router, React, TailwindCSS, Framer Motion)

## Success Criteria
- The landing page matches the wireframe sections exactly.
- Modern and responsive design with Framer Motion animations.
- The UI represents the digital monitoring of public health resources elegantly.

## Tech Stack
- **Next.js**: Framework for the web application
- **TailwindCSS**: Styling
- **Framer Motion**: Animations
- **Lucide React**: Icons

## File Structure
- `src/app/page.tsx`: The main landing page
- `src/app/dashboard/page.tsx`: Moved the existing dashboard here
- Components will be inlined or created in `src/components/` if necessary.

## Task Breakdown

### 1. File Structure Update
- **Name**: Move Dashboard
- **Agent**: `orchestrator`
- **Action**: Move `src/app/page.tsx` to `src/app/dashboard/page.tsx`.
- **Verify**: The old dashboard is accessible at `/dashboard`.

### 2. Implement Hero Section
- **Name**: Hero Component
- **Agent**: `frontend-specialist`
- **Output**: The Hero section with the H1, H2, and CTAs linking to `/dashboard` and external DigiSUS.

### 3. Implement Services Section
- **Name**: Planning Cycle Section
- **Agent**: `frontend-specialist`
- **Output**: 4 interactive cards detailing PS/PMS, PAS, RDQA, and RAG.

### 4. Implement Technology Section
- **Name**: DigiSUS Module Section
- **Agent**: `frontend-specialist`
- **Output**: Features of the DGMP with corresponding Lucide icons.

### 5. Implement Participation Section & Footer
- **Name**: Social Control and Footer
- **Agent**: `frontend-specialist`
- **Output**: Social control text, facts, CTA to resolutions, and responsive footer with links.

## ✅ PHASE X Verification Checklist
- [ ] Build succeeds: `npm run build`
- [ ] Responsive design verified
- [ ] No violet/purple colors (per frontend-specialist rules if applicable)

## ? PHASE X COMPLETE
- Lint: ? Pass
- Security: ? No critical issues
- Build: ? Success
- Date: 2026-03-24
