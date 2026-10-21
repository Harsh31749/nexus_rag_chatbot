# AI & DS II Mini Project: Retrieval-Augmented Generation (RAG) Chatbot

## 📌 Project Overview
This project is an advanced Retrieval-Augmented Generation (RAG) chatbot designed to enable users to upload private PDF documents and query them in real-time. It leverages state-of-the-art Generative AI models (Google Gemini 2.5 Pro) alongside a modern tech stack to provide an intuitive, high-performance web interface.

This repository fulfills the requirements for the AI & DS II Individual Mini Project.

## 🚀 Key Features
- **Document Ingestion:** Upload PDF documents which are instantly parsed and chunked.
- **Vector Search:** Text chunks are embedded using Gemini Embeddings and stored locally in ChromaDB for fast semantic retrieval.
- **Context-Aware Responses:** Queries pull contextually relevant information from the vector store and feed it to the LLM for highly accurate answers.
- **Modern UI:** A functional Web UI built with Next.js, allowing real-time chat and document uploads.

## 🛠️ Technology Stack
- **Frontend:** Next.js (React), Tailwind CSS
- **Backend:** Flask (Python)
- **AI / NLP Pipeline:** LangChain, Google Gemini API
- **Vector Database:** ChromaDB

## 📂 Project Structure
- `/backend`: Contains the Flask server, LangChain RAG pipeline (`app.py`), Exploratory Data Analysis (`EDA_Analysis.ipynb`), and the evaluation script (`evaluate_model.py`).
- `/frontend`: Contains the Next.js Web UI demonstrating real-time predictions.
- `/knowledge_pdf`: Contains sample datasets (PDFs) used for testing.

## 📊 Evaluation Metrics
Since this is a Generative AI model, standard classification metrics (like F1-score or ROC-AUC) are not applicable. Instead, we evaluate the model using **Semantic Similarity**.
An evaluation script (`backend/evaluate_model.py`) calculates the Cosine Similarity between the generated answers and the ground-truth answers for a test dataset. The evaluation metrics report is stored in `backend/evaluation_metrics.txt`.

## ⚙️ Setup Instructions

### 1. Backend Setup
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
Create a `.env` file in the `/backend` directory and add:
```
GEMINI_API_KEY=your_api_key_here
MONGO_URI=mongodb://localhost:27017/
```
Start the backend server:
```bash
python app.py
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:3000` in your browser.

## 👥 Team Contributors
- **Yash** ([@yash1616-accept](https://github.com/yash1616-accept)) — Project Lead, Vector Store Metrics API (`/api/stats`), Setup Documentation
- **Shreyas** ([@Shreyas26X](https://github.com/Shreyas26X)) — Backend Health API (`/api/health`) & Multi-format Document Ingestion
- **Harsh** ([@Harsh31749](https://github.com/Harsh31749)) — Responsive Frontend Web Client & Real-time Chat UI
- **Mahavir** ([@mahavirgujarani04](https://github.com/mahavirgujarani04)) — API Unit Testing, Health Verification & Documentation

