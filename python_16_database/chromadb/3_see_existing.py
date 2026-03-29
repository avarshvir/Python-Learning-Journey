import chromadb

client = chromadb.PersistentClient(path = "./chroma_db")

collection = client.get_collection("vehicles")
print(collection.get())