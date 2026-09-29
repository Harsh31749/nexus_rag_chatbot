import os
import pytest
from io import BytesIO
from unittest.mock import patch, MagicMock

# Import the Flask app from your app.py
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('app.PyPDFLoader')
@patch('app.Chroma')
def test_upload_pdf_success(mock_chroma, mock_pdf_loader, client):
    """Test the document ingestion endpoint."""
    
    # Mock the PDF loading and embedding process
    mock_doc = MagicMock()
    mock_doc.page_content = "dummy document content"
    mock_doc.metadata = {"source": "test_doc.pdf"}
    
    mock_instance = MagicMock()
    mock_instance.load.return_value = [mock_doc]
    mock_pdf_loader.return_value = mock_instance
    
    # Create a fake PDF file in memory
    data = {
        'file': (BytesIO(b"%PDF-1.4 fake pdf content"), 'test_doc.pdf')
    }
    
    response = client.post('/api/upload', data=data, content_type='multipart/form-data')
    
    assert response.status_code == 200
    assert b"Successfully indexed test_doc.pdf" in response.data

def test_upload_no_file(client):
    """Test upload endpoint with missing file."""
    response = client.post('/api/upload', data={})
    
    assert response.status_code == 400
    assert b"No file part" in response.data

@patch('app.vector_store')
@patch('app.llm')
@patch('app.history_collection')
def test_chat_query(mock_history, mock_llm, mock_vector_store, client):
    """Test the RAG chat retrieval endpoint."""
    
    # Mock the vector DB search results
    mock_doc = MagicMock()
    mock_doc.page_content = "This is the retrieved context from the PDF."
    mock_vector_store.similarity_search.return_value = [mock_doc]
    
    # Mock the LLM response
    mock_response = MagicMock()
    mock_response.content = "Based on the context, this is the answer."
    mock_llm.invoke.return_value = mock_response
    
    # Mock database history
    mock_history.find_one.return_value = {"history": []}
    
    payload = {
        "message": "What is in the document?",
        "session_id": "test_session_123"
    }
    
    response = client.post('/api/chat', json=payload)
    
    assert response.status_code == 200
    assert b"Based on the context, this is the answer." in response.data

def test_chat_missing_message(client):
    """Test chat endpoint with empty payload."""
    response = client.post('/api/chat', json={"session_id": "123"})
    
    assert response.status_code == 400
    assert b"Message is required" in response.data