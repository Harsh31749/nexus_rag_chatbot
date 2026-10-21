# 📜 Open Source Project Contribution Report
**Project Name:** Nexus RAG Chatbot (Retrieval-Augmented Generation Document Intelligence System)  
**Repository:** [https://github.com/yash1616-accept/nexus_rag_chatbot](https://github.com/yash1616-accept/nexus_rag_chatbot)  
**License:** MIT Open Source License  
**Academic Submission:** AI & DS II Mini Project  

---

## 🎯 Executive Summary
This document serves as formal evidence of collaborative open-source software development for the **Nexus RAG Chatbot** system. The project was developed following industrial open-source best practices, including git branching workflows, peer pull requests, conventional commits, automated unit testing, and modular separation of concerns.

All four group members contributed distinct features across the full lifecycle: **System Architecture & Analytics**, **Backend Core & Multi-Format Ingestion**, **Web Client Interface**, and **Test Automation & Quality Assurance**.

---

## 👥 Contributor Matrix & Evidence of Work

| Member Name | GitHub Username | Role & Responsibility | Feature / Module Contributed | Git Branch | Commit Hash | Files Impacted |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Yash** | [@yash1616-accept](https://github.com/yash1616-accept) | Project Lead & System Analytics | Vector Store Collection Metrics API (`/api/stats`), portable setup migration, architecture design | `feature/yash-stats-docs` | `9ab766d` | `backend/app.py`, `start.md`, `README.md` |
| **Shreyas** | [@Shreyas26X](https://github.com/Shreyas26X) | Backend Core Engineer | System Health API (`/api/health`), Multi-format Document Ingestion (`.pdf`, `.txt`) | `feature/shreyas-backend-health` | `55246c0` | `backend/app.py` |
| **Harsh** | [@Harsh31749](https://github.com/Harsh31749) | Frontend UI Engineer | Responsive Web Client, Drag-and-Drop Ingestion, Real-time Query Interface | `feature/harsh-web-ui` | `44bbc54` | `frontend/index.html` |
| **Mahavir** | [@mahavirgujarani04](https://github.com/mahavirgujarani04) | QA & DevOps Engineer | Automated Pytest Unit Test Suite, Health Check Verification, Documentation | `feature/mahavir-testing-docs` | `bd096ec` | `backend/test_health.py`, `README.md` |

---

## 📸 How to Present Proof to Evaluators & Examiners

When presenting this project for viva or college evaluation, present the following 4 tangible proofs:

### 1. GitHub Pull Requests Page (Primary Proof)
- Open: `https://github.com/yash1616-accept/nexus_rag_chatbot/pulls?q=is%3Apr`
- Show the 4 merged pull requests with green/purple badges, demonstrating that each member raised a feature PR that was code-reviewed and merged.

### 2. GitHub Insights ➔ Contributors Graph
- Open: `https://github.com/yash1616-accept/nexus_rag_chatbot/graphs/contributors`
- Displays the commits graph and line count for each group member.

### 3. Git Terminal History (`git log`)
Run this command in the terminal to show the visual branch/merge tree:
```bash
git log --graph --pretty=format:"%h - %an (%ad): %s" --date=short
```

### 4. Interactive Live Demo
- Demonstrate **Shreyas's** endpoint: Open `http://localhost:5000/api/health` in browser ➔ shows `{"status": "online", "version": "1.1.0"}`.
- Demonstrate **Yash's** endpoint: Open `http://localhost:5000/api/stats` ➔ shows `{"total_chunks_indexed": ..., "vector_store": "ChromaDB"}`.
- Demonstrate **Harsh's** Web UI: Open `frontend/index.html` ➔ upload `nexus_test_document.pdf` and ask questions.
- Demonstrate **Mahavir's** tests: Run `pytest backend/test_health.py` in the terminal ➔ shows `1 passed in 0.xx seconds`.

---

## 🎤 Viva Voice: Individual Answer Guide

### 🔹 Yash (Project Lead & System Metrics)
- **Question:** *"What did you contribute to this project?"*
- **Answer:** *"I led the project architecture and implemented the `/api/stats` endpoint in Flask. This endpoint inspects the underlying ChromaDB vector collection count in real-time, providing metrics on how many chunks are indexed. I also standardized the environment setup guide to make the project cross-platform."*

### 🔹 Shreyas (Backend Core & Ingestion)
- **Question:** *"What was your role in the backend?"*
- **Answer:** *"I implemented the `/api/health` monitoring endpoint so frontend and cloud systems can ping service availability. I also expanded the document ingestion pipeline in `app.py` to support plain text files (`.txt`) alongside PDFs by integrating LangChain's `TextLoader` with recursive chunking."*

### 🔹 Harsh (Frontend Web UI)
- **Question:** *"How is the frontend structured?"*
- **Answer:** *"I created the web interface in `frontend/index.html`. It is a lightweight, responsive client with an asynchronous document upload zone that talks to the Flask `/api/upload` endpoint, and a real-time conversational chat box that communicates with `/api/chat`."*

### 🔹 Mahavir (Testing & Quality Assurance)
- **Question:** *"How did you test the system?"*
- **Answer:** *"I designed the automated test suite in `backend/test_health.py` using Pytest and Flask's test client fixture. It verifies that HTTP 200 responses and valid JSON payloads are returned without needing to spin up a live server. I also maintained the open-source contributor documentation."*
