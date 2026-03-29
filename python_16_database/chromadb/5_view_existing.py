import chromadb

client = chromadb.PersistentClient(path = "./chroma_db")

collection = client.get_or_create_collection(name="vehicles")

data = collection.get()

print("All documents inside 'vehicles':")
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {doc}")