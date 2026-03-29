import chromadb

# create the client
client = chromadb.Client()

# create collection -- like table in SQL
collection = client.create_collection(name="vehicles")

#print("Collection Created : ", collection.name)
#print("Client DB status : ", client.heartbeat())
#print("See all collections : ", client.list_collections())
#print("how many collections : ", client.count_collections())
#print("wipes everything : ", client.reset())
#print("Chroma version : ", client.get_version())


# Each of chroma collection stores as doc embeding and ids.
# Add Data to collection
collection.add(
    documents=[
        "Car run on land",
        "Plane flies in the skies",
        "Boat travel on water",
        "Bus is public transport on road"
    ],
    ids=["car1", "plane1", "boat1", "bus1"]
)


# Query the collection
results=collection.query(
    query_texts=["vehicle that run on road"],
    n_results=2
)

results2=collection.query(
    query_texts=["If i have to catch fish what should i use"],
    n_results=2
)

# print the output
print(results)
print("--"*5)
print(results2)

