from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import tempfile
import os
from app.utils.pinecone_utils import pinecone_index

def process_pdf(pdf_file):
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        pdf_file.save(tmp_file.name)
        
        # Process PDF
        loader = PyPDFLoader(tmp_file.name)
        document = loader.load()
        texts = [doc.page_content for doc in document]
        combined_text = " ".join(texts)
        
        # Clean up temporary file
        os.unlink(tmp_file.name)

    # Split text
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    chunks = text_splitter.split_text(combined_text)

    # Generate embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)

    # Upload to Pinecone
    vectors_to_upsert = []
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        chunk_id = f"chunk_{i + 1}"
        metadata = {"text": chunk[:500]}
        vectors_to_upsert.append((chunk_id, embedding.tolist(), metadata))

    index = pinecone_index()
    index.upsert(vectors=vectors_to_upsert)
    
    return chunks