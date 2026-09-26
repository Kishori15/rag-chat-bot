from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def semantic_chunk(text,threshold=0.5):
    sentence=[
        s.strip()
        for s in text.split('.')
        if s.strip() 
    ]

    embeddings=model.encode(sentence)

    chunks=[]
    current_chunks=[sentence[0]]

    for i in range(1,len(sentence)):
        similarity=cosine_similarity(
            [embeddings[i - 1]],
            [embeddings[i]]
        )[0][0]

        if similarity>=threshold:
            current_chunks.append(sentence[i])
        else:
            chunks.append(" ".join(current_chunks))
            current_chunks = [sentence[i]]

    chunks.append(" ".join(current_chunks))

    return chunks