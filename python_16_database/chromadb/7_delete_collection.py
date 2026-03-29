import chromadb

# Create a client or Database connection
client = chromadb.PersistentClient(path = "./chroma_db")

# Create a collection or get it if it already exists
collection = client.get_or_create_collection(name = "vehicles")

# Delete the client
#del client
#client.delete_collection(name = "vehicles2")

# Delete the collection
collection.delete(ids=["boat1"])

data = collection.get()
print("All documents inside 'vehicles' after deletion 'boat1':")
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {doc}")