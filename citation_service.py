from sentence_transformers import SentenceTransformer, util
import pinecone

# Initialize Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Pinecone
pinecone.init(api_key="your-pinecone-api-key", environment="us-west1-gcp")
index = pinecone.Index("research-citations")

def find_citations(content: str, num_results: int = 5):
    query_embedding = model.encode(content, convert_to_tensor=True)
    results = index.query(query_embedding.tolist(), top_k=num_results, include_metadata=True)
    citations = [{"title": res["metadata"]["title"], "url": res["metadata"]["url"]} for res in results["matches"]]
    return citations
