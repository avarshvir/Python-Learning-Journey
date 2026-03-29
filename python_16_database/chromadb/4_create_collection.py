import chromadb

# Create a client or Database connection
client = chromadb.PersistentClient(path = "./chroma_db")

# Create a collection or get it if it already exists
collection = client.get_or_create_collection(name = "vehicles")

print("Collection ready: ", collection.name)
print("Collection get: ", collection.get())


# Add some sample data to the collection
collection.add(
    documents=[
        "Car run on land",
        "Plane flies in the skies",
        "Boat travel on water",
        "Bus is public transport on road"
    ],
    ids=["car1", "plane1", "boat1", "bus1"]
)

print("Data added to collection: ", collection.count())
data = collection.get()
print("Collection get: ", data)
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {doc}")

