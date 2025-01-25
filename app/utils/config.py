# config.py
import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

class Config:
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    @classmethod
    def validate(cls):
        missing = []
        if not cls.PINECONE_API_KEY:
            missing.append("PINECONE_API_KEY")
        if not cls.PINECONE_INDEX_NAME:
            missing.append("PINECONE_INDEX_NAME")
        if not cls.GROQ_API_KEY:
            missing.append("GROQ_API_KEY")
        if missing:
            raise EnvironmentError(f"Missing environment variables: {', '.join(missing)}")

# Validate on import
Config.validate()