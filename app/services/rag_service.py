from langchain_huggingface import HuggingFaceEmbeddings  # Updated import
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from app.utils.config import Config
from app.utils.pinecone_utils import pinecone_index
import os  # Add this import

# Set tokenizers parallelism early
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def get_answer(question):
    # Initialize components with updated embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # Updated class
    
    llm = ChatGroq(model_name="Gemma2-9b-It", api_key=Config.GROQ_API_KEY)
    
    # Create vector store
    vector_store = PineconeVectorStore(
        index=pinecone_index(),
        embedding=embeddings,
        text_key="text"
    )

    # Create RAG chain
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )

    # Use invoke() instead of __call__
    response = rag_chain.invoke({"query": question})  # Updated method
    
    return {
        "answer": response["result"],
        "sources": [doc.page_content[:200] for doc in response["source_documents"]]
    }