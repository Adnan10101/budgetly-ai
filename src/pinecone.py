from pinecone import Pinecone, ServerlessSpec
from senetence_transformers import SentenceTransformer
from src.utils.config import PINECONE_API

pinecone = Pinecone(api_key = PINECONE_API)

model = SentenceTransformer("all-MiniLM-L6-v2")

INDEX_NAME = "budgetly-ai"
DIMENSIONS = 384

if INDEX_NAME not in pinecone.list_indexes().names():
    pinecone.crete_index(
        name = INDEX_NAME,
        dimension = DIMENSIONS,
        metric = "cosine",
        spec = ServerlessSpec(cloud = "aws", region = "us-west-2")
    )
index = pinecone.Index(INDEX_NAME)

def get_embeddings(text):
    return model.encode(text).tolist()

def upsert_to_pinecone(data):
    vectors = []
    for page in data:
        #change
        expense_name = page["properties"].get("Expense Name", {}).get("title", [{}])[0].get("text", {}).get("content", "No name")
        amount = page["properties"].get("Amount", {}).get("number", 0)
        text_to_embed = f"{expense_name} - ${amount}"  # Combine fields for embedding

        
        notion_id = page["id"]

       
        embedding = get_embeddings(text_to_embed)

       
        metadata = {
            "expense_name": expense_name,
            "amount": amount,
            "notion_id": notion_id
        }

       
        vectors.append((notion_id, embedding, metadata))

   
    index.upsert(vectors=vectors)
    print(f"Upserted {len(vectors)} records to Pinecone.")