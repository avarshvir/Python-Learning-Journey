import chromadb

# Connect to Persistent Client
client = chromadb.PersistentClient(path = "./chroma_db")

# Create or resuse the collection
collection = client.get_or_create_collection(name="vehicles")

# Add metadata to the collection
collection.add(
    documents=[
        "Car run on land",
        "Plane flies in the skies",
        "Boat travel on water",
        "Bus is public transport on road"
    ],
    ids=["car1", "plane1", "boat1", "bus1"],
    metadatas=[
        {"type": "private_transport", "environment": "land"},
        {"type": "air_transport", "environment": "air"},
        {"type": "water_transport", "environment": "water"},
        {"type": "public_transport", "environment": "land"}
    ]
)

print("Documents added with metadata successfully!")