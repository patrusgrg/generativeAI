from openai import OpenAI
import numpy as np
import faiss
import os

# 1️ Initialize OpenAI client (uses OPENAI_API_KEY env variable)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2️ Your documents
documents = [
    "RAG improves LLM accuracy by retrieving relevant documents.",
    "Large Language Models are trained on massive text datasets.",
    "Transformers use self-attention mechanisms."
]

# 3️ Function to get embeddings
def get_embedding(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    return np.array(response.data[0].embedding)

# 4️ Build FAISS vector store (initialized later)
embeddings = None
index = None

def initialize_faiss():
    global embeddings, index
    embeddings = np.array([get_embedding(doc) for doc in documents], dtype=np.float32)  # <- convert to float32
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

# 5️ Retrieve top-k relevant documents
def retrieve(query, k=2):
    query_emb = get_embedding(query).reshape(1, -1)
    distances, indices = index.search(query_emb, k)
    return [documents[i] for i in indices[0]]

# 6️ Ask LLM using retrieved context
def ask_rag(query, k=2):
    context = "\n".join(retrieve(query, k))
    prompt = f"""
Use the context below to answer the question.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

# 7️ Run example
if __name__ == "__main__":
    initialize_faiss()
    question = "What is RAG?"
    answer = ask_rag(question)
    print("Question:", question)
    print("Answer:", answer)
