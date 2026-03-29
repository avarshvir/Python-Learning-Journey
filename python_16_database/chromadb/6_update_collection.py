import chromadb

# Create a client or Database connection
client = chromadb.PersistentClient(path = "./chroma_db")

# Create a collection or get it if it already exists
collection = client.get_or_create_collection(name = "vehicles")

# Update an existing collection
collection.update(
    ids = ["bus1"],
    documents = ["Bus carries more than 40 passengers and runs on roads"]
)

print("Updated record for bus1: ")
record = collection.get(ids=["bus1"])
print(record)