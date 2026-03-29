import chromadb

client = chromadb.PersistentClient(path = "./chroma_db")

collection = client.get_or_create_collection(name="vehicles_semantic")

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

print("Sample Data Added!")

# Search Semantically
results = collection.query(
    query_texts=["Vehicle that does not need fuel"],
    n_results=1
)

print("Semantic Search Results:")
for doc, dist in zip(results["documents"][0], results["distances"][0]):
    print(f"- {doc} (distance: {dist:.4f})")