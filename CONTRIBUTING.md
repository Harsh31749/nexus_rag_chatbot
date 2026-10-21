# 🤝 Open Source Contributing Guidelines

Thank you for your interest in contributing to **Nexus RAG Chatbot**! This document provides the guidelines and standard workflow for contributing to this open-source project.

---

## 📌 Standard Open-Source Contribution Workflow

All contributors must adhere to the standard Git fork-and-pull workflow:

### 1. Fork the Repository
- Navigate to the upstream repository: `https://github.com/yash1616-accept/nexus_rag_chatbot`
- Click the **Fork** button to create your personal copy under your GitHub account.

### 2. Clone Your Fork
```bash
git clone https://github.com/<your-username>/nexus_rag_chatbot.git
cd nexus_rag_chatbot
```

### 3. Create a Feature Branch
Use descriptive branch naming conventions:
- `feature/<name>-<topic>` (e.g., `feature/shreyas-backend-health`)
- `bugfix/<topic>`
- `test/<topic>`

```bash
git checkout -b feature/<feature-name>
```

### 4. Implement Your Changes
- Keep changes modular and focused on a single deliverable.
- Ensure all existing and new tests pass:
  ```bash
  pytest backend/test_health.py
  ```

### 5. Commit with Conventional Commits
Format your commit messages clearly:
- `feat(module): description`
- `fix(module): description`
- `test(module): description`
- `docs(module): description`

```bash
git add .
git commit -m "feat(backend): add /api/health endpoint and txt document ingestion"
```

### 6. Push and Open a Pull Request (PR)
```bash
git push origin feature/<feature-name>
```
Go to GitHub and submit a **Pull Request** targeting the `main` branch of `yash1616-accept/nexus_rag_chatbot`.

---

## 👥 Verified Core Contributors
- **Yash** — Core RAG Architecture, Vector Store Metrics API (`/api/stats`), Setup Guide
- **Shreyas** — Backend Health API (`/api/health`) & Multi-format Document Ingestion
- **Harsh** — Responsive Frontend Web Client & Real-time Chat UI
- **Mahavir** — Automated Testing Suite & Health Verification
