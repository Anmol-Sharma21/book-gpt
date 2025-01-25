
# BookGPT - PDF QA System

A RAG-based question answering system for PDF documents using Groq, Pinecone, and LangChain.

![API Demo](https://img.shields.io/badge/API-Online-green) 
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)

## Features

- 📄 PDF document processing and text extraction
- 🧠 RAG (Retrieval-Augmented Generation) architecture
- 🔍 Semantic search with Pinecone vector database
- 🤖 LLM-powered answers using Groq's Gemma2-9b-It
- 🚀 REST API endpoints with Flask
- 🔒 Secure configuration with environment variables

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/book-gpt.git
cd book-gpt

# Set up virtual environment and install dependencies
make setup && make install

# Configure environment (edit with your keys)
cp .env.example .env
```

## Usage

```bash
# Start the API server
make run

# API will be available at:
# http://localhost:5000/api/v1/
```

### API Endpoints

**Upload PDF:**
```bash
curl -X POST -F "file=@book.pdf" http://localhost:5000/api/v1/pdf/upload
```

**Ask Question:**
```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"question": "Explain the Krebs cycle"}' \
http://localhost:5000/api/v1/pdf/query
```

## Project Structure

```
.
├── app
│   ├── routes/          # API endpoints
│   ├── services/        # Business logic
│   └── utils/           # Configurations
├── tests
├── .env.example
├── Makefile
├── requirements.txt
└── run.py
```

## Requirements

- Python 3.9+
- Pinecone API key
- Groq API key

## License

MIT License - See [LICENSE](LICENSE) for details
