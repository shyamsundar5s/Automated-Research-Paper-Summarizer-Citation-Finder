from sentence_transformers import SentenceTransformer
import pinecone

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text: str):
    return model.encode(text)

def store_embedding(embedding: list, metadata: dict, index_name: str):
    pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")
    index = pinecone.Index(index_name)
    index.upsert([(metadata["id"], embedding, metadata)])
