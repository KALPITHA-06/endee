import numpy as np

documents = [
    "Artificial Intelligence is the simulation of human intelligence.",
    "Machine Learning is a subset of AI.",
    "Cybersecurity protects systems and data from attacks.",
    "RAG stands for Retrieval Augmented Generation."
]

def simple_search(query):
    for doc in documents:
        if query.lower() in doc.lower():
            return doc
    return "No exact match found, but this is a demo RAG system."

query = input("Ask something: ")
print(simple_search(query))
