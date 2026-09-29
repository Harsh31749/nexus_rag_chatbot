# Viva / External Examiner Preparation Guide
**Project:** Retrieval-Augmented Generation (RAG) Chatbot

This guide will help you confidently explain your project to an external examiner, focusing on architecture, model understanding, and implementation details.

## 1. The "Elevator Pitch" (How to introduce your project)
**"My project is a Retrieval-Augmented Generation (RAG) Chatbot. It allows users to upload private PDF documents, and then uses a Large Language Model (Google Gemini) to answer questions based *only* on the uploaded documents. This solves the problem of LLMs hallucinating or lacking private/domain-specific knowledge."**

## 2. Architecture & Flow (How it works under the hood)
If the examiner asks: *"Explain the flow of your application."*
1. **Document Ingestion:** The user uploads a PDF via the Next.js frontend. The Flask backend receives it and uses LangChain (`PyPDFLoader`) to read the text.
2. **Chunking:** The text is split into smaller pieces (500 characters each) using a `RecursiveCharacterTextSplitter`. We do this because LLMs have a context limit, and searching through massive blocks of text is inefficient.
3. **Embedding:** These chunks are converted into numerical vectors using Google's `gemini-embedding-2` model. Vectors capture the *semantic meaning* of the text.
4. **Vector Database:** The vectors are stored in **ChromaDB** (a local vector database).
5. **Retrieval & Generation:** When the user asks a question, the question is also converted into a vector. ChromaDB performs a "similarity search" (Cosine Similarity) to find the most relevant document chunks. Those chunks are then sent to the LLM (`gemini-2.5-flash`) along with the question, and the LLM generates a human-like response.

## 3. Anticipated Viva Questions & Answers

### Q: Why did you choose RAG instead of Fine-Tuning the model?
**A:** Fine-tuning is computationally expensive, requires a massive labeled dataset, and is hard to update if the data changes. RAG is dynamic—if I upload a new PDF, the model instantly knows the new information without any retraining. RAG also drastically reduces hallucinations because the LLM is forced to look at the retrieved text.

### Q: What Evaluation Metrics did you use? Why not F1-score or Accuracy?
**A:** Traditional metrics like F1-score or ROC-AUC are meant for classification tasks (e.g., Is this spam or not?). Because this is a Generative AI model, there is no strict "True/False" output. Instead, I wrote an evaluation script using `scikit-learn` to calculate **Semantic Cosine Similarity** between the generated answer and a known ground-truth answer. A high similarity score (e.g., > 0.85) proves the model accurately retrieved and synthesized the right information.

### Q: What is the role of ChromaDB?
**A:** ChromaDB is a Vector Database. Traditional SQL databases search for exact keyword matches. ChromaDB stores mathematical vectors and searches based on "Semantic Similarity." This means if a user asks about "Space missions," it will retrieve text about "Mars base," even if the word "Space" isn't strictly in the text.

### Q: Why did you split the text into chunks? (EDA aspect)
**A:** If we feed an entire 100-page PDF to an LLM, it exceeds the context window and dilutes the semantic search accuracy. By chunking (e.g., 500 characters with a 50-character overlap), we ensure the vector database retrieves highly specific, targeted paragraphs. My EDA (Jupyter Notebook) visualizes this chunk distribution.

## 4. Demonstrating Code Cleanliness & Individual Work
- Be ready to open `backend/app.py` and show the `/api/upload` and `/api/chat` endpoints. Point out how cleanly the LangChain pipeline is integrated.
- Show them the Next.js frontend code to prove you built a modern, interactive UI, not just a simple script.
- Show them the `evaluate_model.py` script to demonstrate that you didn't just string APIs together, but actually measured the mathematical accuracy of the system using Python and Scikit-learn.
