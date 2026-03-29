import chromadb

# Connect to Persistent Client
client = chromadb.PersistentClient(path = "./chroma_db")

# Create or resuse the collection
collection = client.get_or_create_collection(name="vehicles")

# retrieve all documents with metadata
data = collection.get(include=["documents", "metadatas"])
print("Documents with metadata:")
for i, doc, meta in zip(data["ids"], data["documents"], data["metadatas"]):
    print(f"ID: {i} -> Document: {doc} | Metadata: {meta}")
 