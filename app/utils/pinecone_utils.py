from pinecone import Pinecone, ServerlessSpec
from app.utils.config import Config

pc = Pinecone(api_key=Config.PINECONE_API_KEY)

def pinecone_index():
    if Config.PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=Config.PINECONE_INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )
    return pc.Index(Config.PINECONE_INDEX_NAME)