# 🧠 Vichintarka — Product & Technical PRD

**Version:** 1.0  
**Date:** 2025-10-06  
**Author:** Aakash Malik

---

## 📑 Table of Contents

- [Part I: 📝 Product PRD — Vision, Strategy, and Functional Scope](#part-i--product-prd--vision-strategy-and-functional-scope)
  - [1. Executive Summary](#1-executive-summary)
  - [2. Vision & Philosophy](#2-vision--philosophy)
  - [3. Core Concept & Differentiation](#3-core-concept--differentiation)
  - [4. Market Context & Opportunity](#4-market-context--opportunity)
  - [5. Target Users & Personas](#5-target-users--personas)
  - [6. Problem Statement](#6-problem-statement)
  - [7. Product Objectives](#7-product-objectives)
  - [8. Guiding Principles](#8-guiding-principles)
  - [9. Product Scope & Non-scope](#9-product-scope--non-scope)
  - [10. Core Features (Functional Requirements)](#10-core-features-functional-requirements)
  - [11. User Roles & Permissions](#11-user-roles--permissions)
  - [12. User Journey Flow](#12-user-journey-flow)
  - [13. Platform Structure & Multi-tenancy](#13-platform-structure--multi-tenancy)
  - [14. Content Hierarchy & Taxonomy](#14-content-hierarchy--taxonomy)
  - [15. Exam Flow & Grading Rules](#15-exam-flow--grading-rules)
  - [16. Analytics & Insights Framework](#16-analytics--insights-framework)
  - [17. Browser Lockdown & Anti-cheat](#17-browser-lockdown--anti-cheat)
  - [18. Design Principles & UX Guidelines](#18-design-principles--ux-guidelines)
  - [19. MVP Deliverables](#19-mvp-deliverables)
  - [20. Phase 2 and Advanced Features](#20-phase-2-and-advanced-features)
  - [21. Success Metrics (KPIs)](#21-success-metrics-kpis)
  - [22. Monetization Strategy (Future)](#22-monetization-strategy-future)
  - [23. Competitive Landscape](#23-competitive-landscape)
  - [24. Risks & Assumptions](#24-risks--assumptions)
  - [25. Future Vision](#25-future-vision)

- [Part II: 🧰 Technical PRD — Architecture, Stack, and Implementation](#part-ii--technical-prd--architecture-stack-and-implementation)
  - [26. Technical Overview](#26-technical-overview)
  - [27. System Architecture (Microservices Layout)](#27-system-architecture-microservices-layout)
  - [28. Technology Stack](#28-technology-stack)
  - [29. Service Definitions](#29-service-definitions)
  - [30. Database Design (Key Tables)](#30-database-design-key-tables)
  - [31. API Design (REST)](#31-api-design-rest)
  - [32. Authentication & Authorization](#32-authentication--authorization)
  - [33. Multi-tenancy Implementation](#33-multi-tenancy-implementation)
  - [34. File Storage & Media Management](#34-file-storage--media-management)
  - [35. PDF Generation Service](#35-pdf-generation-service)
  - [36. Real-time Exam Timers & Enforcement](#36-real-time-exam-timers--enforcement)
  - [37. Anti-cheat Browser Enforcement](#37-anti-cheat-browser-enforcement)
  - [38. Caching & Performance](#38-caching--performance)
  - [39. Logging, Monitoring & Error Tracking](#39-logging-monitoring--error-tracking)
  - [40. Deployment Architecture](#40-deployment-architecture)
  - [41. CI/CD Pipeline](#41-cicd-pipeline)
  - [42. Security Framework](#42-security-framework)
  - [43. Scalability & Load Handling](#43-scalability--load-handling)
  - [44. Backup & Disaster Recovery](#44-backup--disaster-recovery)
  - [45. Testing Strategy](#45-testing-strategy)
  - [46. Analytics & Telemetry](#46-analytics--telemetry)
  - [47. Environment Configuration](#47-environment-configuration)
  - [48. Development Milestones & Sprints](#48-development-milestones--sprints)
  - [49. Future Technical Extensions](#49-future-technical-extensions)
  - [50. Final Summary & Evolution Path](#50-final-summary--evolution-path)

---

## Part I: 📝 Product PRD — Vision, Strategy, and Functional Scope

### 1. Executive Summary

Vichintarka is a **multi-tenant online exam preparation platform** designed to help students systematically practice, attempt, and analyze questions for competitive exams such as **JEE Main**, **JEE Advanced**, and **NEET**.  

The platform emphasizes **reasoning**, **reflection**, and **analytical learning** by providing structured tests, per-question insights, and practice modules with discussion and reporting features.

The initial release (MVP) targets **students only**, with support for multiple exam organizations as separate tenants.  

Vichintarka integrates:
- ✉️ Email verification  
- 🔐 Google OAuth  
- 🧭 Browser-based anti-cheat enforcement  
- 📝 PDF generation for tests and solutions

---

### 2. Vision & Philosophy

> “Empower students to think, reason, and master exam knowledge through structured practice and reflective learning.”

Vichintarka embodies the union of **Viveka (discernment)**, **Chintana (thought)**, **Tarka (logic)**, and **Manana (reflection)** — ensuring a learning experience rooted in clarity, analysis, and insight.

---

### 3. Core Concept & Differentiation

- 🏢 **Multi-tenant structure** allows each exam or organization to manage independent question banks and tests.  
- 📚 **Comprehensive question types**: MCQ (single/multiple), numerical, matching, matrix, image-based, passage-based with sub-questions.  
- 📊 **Advanced analytics**: Per-question and per-student insights, topic-wise performance tracking.  
- 🧠 **Practice and discussion**: Students can attempt questions outside tests, comment, and report issues.  
- 📝 **PDF generation**: Question papers, answer keys, and solution sheets downloadable post-test.  
- 🔒 **Anti-cheat features**: Browser tab-switch detection and enforced full-screen mode during exams.

---

### 4. Market Context & Opportunity

- Online exam prep in India is a growing multi-billion-dollar market, dominated by **Byju’s**, **Unacademy**, **Aakash**, etc.  
- Students require platforms that combine adaptive practice with structured assessment.  
- Vichintarka differentiates by providing **exam-specific multi-tenancy**, **deep analytics**, and **structured content hierarchy** from day one.

---

### 5. Target Users & Personas

**Primary Users:**  
- Students (ages 16–22) preparing for competitive exams.

**User Persona Example:**  
- **Name:** Rohan Sharma  
- **Age:** 18  
- **Exam:** JEE Main  
- **Goals:** Maximize accuracy in practice tests, identify weak topics, download solutions for offline study.

---

### 6. Problem Statement

Students lack integrated platforms that combine **practice**, **testing**, **analytics**, and **exam-specific content** in one place.  
Current solutions either emphasize content consumption or live classes but do not provide **reflective insights post-attempt**.

---

### 7. Product Objectives

- Deliver **multi-tenant exam-specific** question and test management.  
- Provide **per-question and per-topic insights**.  
- Ensure **secure, timed, and anti-cheat exam attempts**.  
- Enable **offline study via PDFs**.

---

### 8. Guiding Principles

- 🧭 **Student-first:** Minimal friction, intuitive UX.  
- 📈 **Data-driven:** Insights should guide learning.  
- 🧩 **Scalable & Modular:** Microservices architecture for future growth.  
- 🔐 **Secure & Reliable:** Protect user data and exam integrity.

---

### 9. Product Scope & Non-scope

**In-scope (MVP):**  
- Multi-tenant exam management  
- Student sign-up/login (email + Google OAuth)  
- Pre-built timed tests with auto-grading  
- Practice mode with discussion threads  
- PDF generation for question papers & solutions  
- Per-question and per-topic analytics

**Out-of-scope (v1):**  
- AI-based recommendations  
- Adaptive testing  
- Mobile app (only responsive web)  
- Payment and subscription management

---

### 10. Core Features (Functional Requirements)

**Authentication & Authorization**  
- Email verification + Google OAuth  
- JWT-based session management  
- Student-only role (v1)

**Organization & Content Hierarchy**  
- Organizations → Subjects → Topics → Questions  
- Tagging: Subject, Topic, Difficulty, Bloom’s taxonomy

**Question Bank**  
- Multiple types (MCQ, numerical, matching, matrix, image, passage)  
- LaTeX rendering  
- Images for questions  
- Versioned correct answers (visible post-test)

**Tests & Attempts**  
- Section-wise timing, negative marking, partial credits  
- Client + server timer enforcement  
- Auto-submit on time expiry or tab switch  
- Downloadable PDFs

**Practice Mode**  
- Individual question practice  
- Commenting, upvotes, reporting

**Analytics & Insights**  
- Per-question, per-section, per-student  
- Cohort benchmarking  
- Exportable as CSV/PDF

---

### 11. User Roles & Permissions

| Role    | Permissions |
|--------|-------------|
| Student | Attempt tests, view results, practice questions, comment/report |
| Admin (future) | Manage organizations, subjects, topics, questions, users |

---

### 12. User Journey Flow

1. Signup/Login → Dashboard → Select Organization  
2. Practice Mode → Browse Topics → Attempt Questions → Comment/Report  
3. Test Mode → Start Timed Test → Auto-Submission → Analytics  
4. Download PDFs → Review Solutions → Repeat Practice

---

### 13. Platform Structure & Multi-tenancy

- Each organization represents an exam (e.g., JEE Main, NEET).  
- Users are linked to organizations; each org has its own subjects, topics, questions, and tests.

---

### 14. Content Hierarchy & Taxonomy

- Subjects → Topics → Subtopics → Questions  
- Questions tagged by type, difficulty, topic, Bloom’s taxonomy  
- Media support: Images (inline), LaTeX (math), PDF solutions

---

### 15. Exam Flow & Grading Rules

- Section-wise timing  
- Negative marking  
- Partial credits  
- Auto-grading for objective questions  
- Browser lockdown for anti-cheat

---

### 16. Analytics & Insights Framework

- Track accuracy per question, topic, and student  
- Compute average time per question  
- Identify weak areas  
- Exportable reports

---

### 17. Browser Lockdown & Anti-cheat

- Full-screen enforced during test  
- Detect tab switching → flag or auto-submit  
- No webcam / offline capture in v1

---

### 18. Design Principles & UX Guidelines

- Clean, responsive UI (**Vue.js + TailwindCSS**)  
- Timer visible at top during tests  
- Clear rendering of question text + images + LaTeX  
- Accessible color schemes, keyboard navigation

---

### 19. MVP Deliverables

- ✅ Multi-tenant structure  
- 🧪 Pre-built test flow with timers & scoring  
- 🧠 Practice mode + discussion threads  
- 📊 Per-question analytics  
- 📝 PDF generation for papers & solutions  
- 🔐 Google OAuth + Email auth

---

### 20. Phase 2 and Advanced Features

- 🤖 AI-based difficulty estimation  
- 🧭 Adaptive test generation  
- 📱 Mobile app (iOS/Android)  
- 💳 Subscription & payment features  
- 📈 Advanced analytics dashboards

---

### 21. Success Metrics (KPIs)

- MAU/DAU (students logging in)  
- Test completion rate  
- Average score improvement  
- Active practice attempts  
- PDF download counts

---

### 22. Monetization Strategy (Future)

- Freemium model with subscription tiers  
- Coupons, promo codes, referral system

---

### 23. Competitive Landscape

- Major players: Byju’s, Unacademy, Vedantu  
- **Differentiation:** Multi-tenant, deep analytics, lightweight web-first, exam-specific

---

### 24. Risks & Assumptions

- ⚠️ **Risk:** Student engagement may be low without adaptive tests  
- 💭 **Assumption:** Users have stable internet access  
- 🛠 **Mitigation:** Focus on practice + PDF solutions

---

### 25. Future Vision

- 🤖 AI-powered question recommendation  
- 🧭 Adaptive learning paths  
- 🏫 Integration with institutional dashboards  
- 📱 Mobile apps and offline support

---

## Part II: 🧰 Technical PRD — Architecture, Stack, and Implementation

### 26. Technical Overview

- **Backend:** FastAPI (async)  
- **Database:** PostgreSQL 15+ (multi-tenant aware)  
- **ORM:** SQLAlchemy + Pydantic models  
- **Frontend:** Vue.js 3 + TailwindCSS + Vite  
- **Caching & Queue:** Redis  
- **Storage:** AWS S3 for media & PDFs  
- **Deployment:** Dockerized microservices, AWS ECS/EC2

---

### 27. System Architecture (Microservices Layout)

---

### 28. Technology Stack

- **Backend:** Python 3.12+, FastAPI, SQLAlchemy 2.0  
- **Frontend:** Vue.js 3, TailwindCSS, Axios, Vite  
- **DB:** PostgreSQL 15+, Alembic migrations  
- **Caching/Queue:** Redis, RQ or Celery  
- **File storage:** AWS S3  
- **Auth:** OAuth2 (Google), JWT  
- **Containerization:** Docker + Docker Compose  
- **Deployment:** AWS ECS / EC2, Nginx reverse proxy

---

### 29. Service Definitions

- **Auth Service:** User management, OAuth, JWT, multi-tenancy  
- **Organization Service:** Exam/organization CRUD, subjects, topics  
- **Question Service:** CRUD questions, media, comments, reporting  
- **Test Service:** Pre-built tests, timed attempts, scoring  
- **Analytics Service:** Per-question, per-student stats, exportable  
- **File Service:** PDF generation, image uploads

---

### 30. Database Design (Key Tables)

- `organizations`, `users`, `subjects`, `topics`, `questions`, `options`, `tests`, `test_questions`, `attempts`, `attempt_answers`  
- Multi-tenant-aware schema  
- JSONB columns for flexible question options and test structures

---

### 31. API Design (REST)

- `/auth/*`, `/organizations/*`, `/questions/*`, `/tests/*`, `/attempts/*`, `/analytics/*`  
- JWT token validation, role-based access  
- Rate-limiting and input validation

---

### 32. Authentication & Authorization

- JWT tokens (short-lived access + refresh)  
- Google OAuth 2.0 integration  
- Role-based access: student, admin (future)  
- Email verification flow

---

### 33. Multi-tenancy Implementation

- Organization ID in all tables  
- Scoped queries per organization  
- Tenant-aware caching and analytics

---

### 34. File Storage & Media Management

- AWS S3 for images & PDFs  
- Signed URLs for secure access  
- Background task for PDF generation

---

### 35. PDF Generation Service

- ReportLab / WeasyPrint for PDFs  
- Generates question papers, answer keys, solutions  
- Stored in S3 and accessible via signed URL

---

### 36. Real-time Exam Timers & Enforcement

- Client-side timer with autosave  
- Backend enforcement via timestamp comparison  
- Auto-submit on expiry or anti-cheat event

---

### 37. Anti-cheat Browser Enforcement

- Fullscreen mode enforced  
- Detect tab switching → flag or auto-submit  
- Event logs stored for auditing

---

### 38. Caching & Performance

- Redis for session cache, frequently accessed questions, leaderboard/analytics cache  
- Async DB queries in FastAPI

---

### 39. Logging, Monitoring & Error Tracking

- Centralized logging via CloudWatch or ELK  
- Error tracking via Sentry or Rollbar  
- Performance metrics monitored via Prometheus + Grafana

---

### 40. Deployment Architecture

- Dockerized microservices  
- AWS ECS or EC2 + Nginx reverse proxy  
- Environment separation: Dev → Staging → Production  
- CI/CD via GitHub Actions

---

### 41. CI/CD Pipeline

- Unit + integration tests → build → push docker image → deploy  
- Automated DB migrations via Alembic  
- Deployment scripts for ECS

---

### 42. Security Framework

- Input validation, XSS/SQL injection prevention  
- HTTPS enforced via SSL (ACM or Let’s Encrypt)  
- JWT with secure cookies  
- Role-based access control

---

### 43. Scalability & Load Handling

- Microservices allow horizontal scaling per domain  
- Redis caching for high concurrency  
- Async FastAPI handles 1000+ concurrent users

---

### 44. Backup & Disaster Recovery

- Daily DB backups (Postgres RDS snapshots)  
- S3 versioning for media/PDFs  
- Recovery plan tested quarterly

---

### 45. Testing Strategy

- Unit tests: Pytest  
- Integration tests for services  
- Load testing for exam concurrency  
- End-to-end test automation

---

### 46. Analytics & Telemetry

- Per-question, per-student analytics stored in PostgreSQL + Redis cache  
- Exportable CSV/PDF reports  
- Event logging for insights

---

### 47. Environment Configuration

- `.env` files for secret keys  
- Separate Dev / Stage / Prod configurations  
- AWS IAM roles for access control

---

### 48. Development Milestones & Sprints

- **Sprint 1:** Auth + Organization + DB setup  
- **Sprint 2:** Question CRUD + Test CRUD  
- **Sprint 3:** Test attempt flow + client timer + browser lockdown  
- **Sprint 4:** Practice mode + comment/report features  
- **Sprint 5:** Analytics + PDF generation + caching  
- **Sprint 6:** Final QA + Deployment + Monitoring

---

### 49. Future Technical Extensions

- 🤖 AI-powered difficulty estimation and analytics  
- 🧭 Adaptive test engine  
- 🧠 Recommendation engine for practice questions  
- 📱 Mobile app integration

---

### 50. Final Summary & Evolution Path

Vichintarka combines **philosophical depth** with **modern engineering**, delivering a **scalable**, **secure**, **multi-tenant** exam preparation platform.  

Its architecture ensures modular expansion, high performance, and analytic insights, positioning it as a robust foundation for future **AI-powered educational innovations**. 🚀

---