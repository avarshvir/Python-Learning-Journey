import numpy as np
import chromadb

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

client = chromadb.PersistentClient(path = "./chroma_db")
collection = client.get_or_create_collection(name="vehicles_embeddings")


data = collection.get(include=["documents", "embeddings"])

# Get Embeddings
emb_cars = data["embeddings"][0]  # Cars run on petrol
emb_bus = data["embeddings"][1]   # Bus carries passengers
emb_bicycle = data["embeddings"][2]  # Bicycle run without fuel
emb_boat = data["embeddings"][3]  # Boat travel on water
emb_plane = data["embeddings"][4]  # Plane flies in the sky

# Compare similarities
sim_car_bus = cosine_similarity(emb_cars, emb_bus)
sim_car_bicycle = cosine_similarity(emb_cars, emb_bicycle)

print(f"Car vs Bus : {sim_car_bus:.4f}")
print(f"Car vs Bicycle : {sim_car_bicycle:.4f}")

