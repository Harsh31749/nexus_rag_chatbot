import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import time
import requests

load_dotenv()

# Ground truth dataset for evaluation
eval_data = [
    {
        "question": "What is the override code for the Level 3 diagnostic terminal?",
        "ground_truth": "The override code is 'NEXUS-99-OMEGA'."
    },
    {
        "question": "Who is the Lead Architect?",
        "ground_truth": "Dr. Aris Thorne."
    },
    {
        "question": "What is the maximum temperature threshold for the system?",
        "ground_truth": "4.2 Kelvin."
    }
]

# Initialize embeddings for evaluation
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-2", google_api_key=os.getenv("GEMINI_API_KEY"))

print("Starting RAG Evaluation...")
results = []
similarity_scores = []

for item in eval_data:
    question = item["question"]
    truth = item["ground_truth"]
    
    # Call the local Flask API
    try:
        response = requests.post("http://127.0.0.1:5000/api/chat", json={"message": question})
        if response.status_code == 200:
            generated_answer = response.json().get("response", "")
        else:
            generated_answer = "Error"
    except Exception as e:
        generated_answer = str(e)
        
    print(f"\nQ: {question}")
    print(f"Generated: {generated_answer}")
    print(f"Truth: {truth}")
    
    if generated_answer and generated_answer != "Error":
        # Calculate semantic similarity between generated answer and ground truth
        truth_emb = embeddings.embed_query(truth)
        gen_emb = embeddings.embed_query(generated_answer)
        
        sim = cosine_similarity([truth_emb], [gen_emb])[0][0]
        similarity_scores.append(sim)
        print(f"Semantic Similarity (Cosine): {sim:.4f}")
    
    time.sleep(1) # rate limit prevention

if similarity_scores:
    mean_sim = np.mean(similarity_scores)
    print(f"\n=== EVALUATION METRICS ===")
    print(f"Average Semantic Similarity (Accuracy Proxy): {mean_sim:.4f}")
    print(f"Total Evaluated: {len(similarity_scores)}/{len(eval_data)}")
    
    with open("evaluation_metrics.txt", "w") as f:
        f.write("=== RAG MODEL EVALUATION METRICS ===\n")
        f.write(f"Average Semantic Similarity Score: {mean_sim:.4f}\n")
        f.write("Note: This metric serves as an analogue to accuracy/F1-score for generative models, representing how closely the generated answer matches the ground truth semantically.\n")
