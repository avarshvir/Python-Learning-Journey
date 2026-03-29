import chromadb

# Connect to Persistent Client
client = chromadb.PersistentClient(path = "./chroma_db")

# Create or resuse the collection
collection = client.get_or_create_collection(name="vehicles")

# Filter by transport type
public_transport = collection.get(
    where={"type": "public_transport"}
) 

print("Public transport documents:")
print(public_transport)

water_transport  = collection.get(
    where={"environment": "water"}
)

print("Water transport documents:")
print(water_transport)
