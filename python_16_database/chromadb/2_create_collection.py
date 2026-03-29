import chromadb

# create DB client
client = chromadb.PersistentClient(path = "./chroma_db")

# create Collection
collection = client.create_collection(name="vehicles")

# add data
collection.add(
    documents = [
        "Car run on land",
        "Plane flies in the skies",
        "Boat travel on water",
        "Bus is public transport on road"
    ],
    ids = ["car1", "plane1", "boat1", "bus1"]
)

"""
# query the collection
result = collection.query(
    query_texts=["vehicle that run on road"],
    n_results=2
)"""

print("Data is saved permanentaly")