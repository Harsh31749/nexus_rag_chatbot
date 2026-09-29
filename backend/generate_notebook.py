import nbformat as nbf

nb = nbf.v4.new_notebook()

text = """\
# Exploratory Data Analysis (EDA) for RAG Chatbot
This notebook analyzes the document corpus used for the Retrieval-Augmented Generation (RAG) system. 
In a RAG system, the 'dataset' consists of documents. Our EDA focuses on:
1. Document text length and structure.
2. Text chunking analysis (crucial for vector embedding).
3. Word frequency distribution to understand the primary topics.
"""

code_1 = """\
import os
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the PDF Document
# We will use the test PDF generated earlier.
pdf_path = '../knowledge_pdf/nexus_test_document.pdf'
loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"Number of pages loaded: {len(documents)}")
"""

code_2 = """\
# Extract raw text from all pages
full_text = " ".join([doc.page_content for doc in documents])
print(f"Total characters in document: {len(full_text)}")
print(f"Total words in document: {len(full_text.split())}")
"""

code_3 = """\
# Text Chunking Analysis
# In RAG, we split text into chunks before embedding. 
# We need to analyze if our chunk size fits the context window properly.

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

chunk_lengths = [len(chunk.page_content) for chunk in chunks]
print(f"Total chunks created: {len(chunks)}")

# Plotting Chunk Size Distribution
plt.figure(figsize=(8, 5))
sns.histplot(chunk_lengths, bins=20, kde=True, color='blue')
plt.title('Distribution of Chunk Lengths (Characters)')
plt.xlabel('Chunk Length')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()
"""

code_4 = """\
# Word Frequency Analysis
# Identifying the most common words helps us understand the document's main topics.

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return text

cleaned_text = clean_text(full_text)
words = cleaned_text.split()

# Remove basic stop words manually for simplicity
stop_words = {'the', 'a', 'to', 'of', 'and', 'in', 'is', 'for', 'on', 'this', 'that', 'with', 'as', 'by', 'are'}
filtered_words = [w for w in words if w not in stop_words and len(w) > 2]

word_counts = Counter(filtered_words)
common_words = word_counts.most_common(15)

# Plotting Top Words
words_list, counts_list = zip(*common_words)

plt.figure(figsize=(10, 6))
sns.barplot(x=list(counts_list), y=list(words_list), palette='viridis')
plt.title('Top 15 Most Frequent Words in the Document')
plt.xlabel('Count')
plt.ylabel('Word')
plt.show()
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text),
    nbf.v4.new_code_cell(code_1),
    nbf.v4.new_code_cell(code_2),
    nbf.v4.new_code_cell(code_3),
    nbf.v4.new_code_cell(code_4)
]

with open('EDA_Analysis.ipynb', 'w') as f:
    nbf.write(nb, f)
print("EDA_Analysis.ipynb generated successfully.")
