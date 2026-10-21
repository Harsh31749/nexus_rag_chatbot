# 🚀 Getting Started & Testing Guide

This document contains step-by-step instructions to run your RAG Chatbot and test all the deliverables for your AI & DS II Mini Project.

---

## 1️⃣ Start the Backend (Flask + Gemini + ChromaDB)

You must start the backend server first. It handles document ingestion, vector storage, and communicating with the Gemini API.

1. Open a new terminal (PowerShell or Command Prompt).
2. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
3. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
4. Start the server:
   ```bash
   python app.py
   ```
**Expected Output:** You should see `* Running on http://127.0.0.1:5000`. Keep this terminal open!

---

## 2️⃣ Open the Web UI (Frontend)

Next, launch the web interface to upload documents and query the chatbot.

1. Open `frontend/index.html` directly in your web browser (double-click the file or open it in Chrome/Edge).
2. Alternatively, use a lightweight HTTP server:
   ```bash
   npx serve frontend
   ```

---

## 3️⃣ Test the Web UI (Manual Testing)

1. Open the UI in your browser (`frontend/index.html`).
2. **Upload a Document:** 
   - Click the file picker and select a test document (e.g., `knowledge_pdf/nexus_test_document.pdf`).
   - Click **Upload & Index**.
   - Wait for the "Successfully indexed" success message.
3. **Ask Questions:** 
   - Type: *"Who is the Lead Architect?"*
   - The chatbot should reply: *"Dr. Aris Thorne"*.
   - Type: *"What is the override code for the Level 3 terminal?"*
   - The chatbot should reply with *"NEXUS-99-OMEGA"*.

---

## 4️⃣ Run the RAG Evaluation Script (Deliverable 2)

We created a custom evaluation script to calculate the accuracy (Semantic Similarity) of your RAG pipeline. **Make sure your backend (`app.py`) is already running in step 1 before running this!** 

*(Note: Earlier this failed for you because the backend server was stopped. Make sure it is running!)*

1. Open a **third** terminal.
2. Navigate to the backend and activate the virtual environment:
   ```bash
   cd backend
   .\venv\Scripts\activate
   ```
3. Run the evaluation script:
   ```bash
   python evaluate_model.py
   ```
**Expected Output:** The script will query your live backend automatically, compare the answers to the "ground truth", and output an accuracy score to the terminal and to a file named `evaluation_metrics.txt`.

---

## 5️⃣ View the Exploratory Data Analysis (Deliverable 1)

I already generated your Jupyter Notebook (`EDA_Analysis.ipynb`). To view it:

1. Inside your active backend terminal (or VS Code), ensure Jupyter is installed:
   ```bash
   pip install jupyter
   ```
2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
3. In the browser window that opens, click on `EDA_Analysis.ipynb` and click **"Run All"** to view your beautiful text chunking and word frequency charts!
