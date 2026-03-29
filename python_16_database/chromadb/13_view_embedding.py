import chromadb

client = chromadb.PersistentClient(path = "./chroma_db")
collection = client.get_or_create_collection(name="vehicles_embeddings")

# retrive the embedding for each document
data = collection.get(include=["documents", "embeddings"])


for i, text, embed in zip(data["ids"], data["documents"], data["embeddings"]):
    print(f"\n {i} : {text}")
    print(f"\n Embedding (first 10 values): {embed[:10]}")