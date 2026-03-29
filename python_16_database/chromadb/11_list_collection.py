import chromadb

# Connect to Persistent Client
client = chromadb.PersistentClient(path = "./chroma_db")

collection = client.list_collections()

print("Collections in the database:")
for c in collection:
    print(c.name)
    print(c)
    
