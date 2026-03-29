import chromadb

client = chromadb.PersistentClient(path = "./chroma_db")

collection = client.get_or_create_collection(name="vehicles_embeddings")

print("Collection created or reused successfully.")
print("Collection name:", collection.name)

    
collection.add(
    documents=[
        "Cars run on petrol",
        "Bus carries pasangers",
        "Bicycle run without fuel",
        "Boat travel on water",
        "Plane flies in the sky"
    ],
    ids = ["car1", "bus1", "bicycle1", "boat1", "plane1"]
)

print("Documents added with embeddings automatically generated.")