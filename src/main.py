"""
main.py

Entry point for the tiny RAG retrieval system.

Pipeline:

1. Load documents from disk
2. Split documents into retrievable chunks
3. Generate embeddings for each chunk
4. Initialize semantic retriever
5. Generate embedding for user query
6. Retrieve most relevant chunks
7. Display retrieval results
"""

from config import DOCUMENTS_PATH
from loader import loader_function
from chunker import Chunker
from embedding import EmbeddingGenerator
from retriever import Retriever


# ====================================
# 1. Load documents
# ====================================

documents = loader_function(DOCUMENTS_PATH)

if not documents:
    print("No documents found.")
    exit()


print("\n==============================")
print("Corpus Loaded")
print("==============================")

print(f"Documents loaded: {len(documents)}")


# ====================================
# 2. Chunk documents
# ====================================

chunker = Chunker()

all_chunks = []

for document in documents:
    chunks = chunker.chunk(document)
    all_chunks.extend(chunks)


print("\n==============================")
print("Chunking Complete")
print("==============================")

print(f"Total chunks created: {len(all_chunks)}")


# ====================================
# 3. Generate chunk embeddings
# ====================================

generator = EmbeddingGenerator()

print("\n==============================")
print("Generating Chunk Embeddings")
print("==============================")


for chunk in all_chunks:
    chunk.embedding = generator.generate(
        chunk.text
    )


print(f"Embedded {len(all_chunks)} chunks.")

# ====================================
# 4. Initialize Retriever
# ====================================

retriever = Retriever(all_chunks)


# ====================================
# 5. User Query
# ====================================

user_query = "What is RAG pipeline?"

print("\n==============================")
print("Search Query")
print("==============================")

print(user_query)


# ====================================
# 6. Generate query embedding
# ====================================

query_embedding = generator.generate(
    user_query
)


print("\nQuery embedding generated.")
print(f"Dimensions: {len(query_embedding)}")
print(f"First 5 values: {query_embedding[:5]}")


# ====================================
# 7. Retrieve relevant chunks
# ====================================

results = retriever.search(
    query_embedding,
    top_k=3,
)


# ====================================
# 8. Display results
# ====================================

print("\n==============================")
print("Retrieval Results")
print("==============================")


for rank, (chunk, score) in enumerate(results, start=1):

    print(f"\nRank {rank}")
    print(f"Chunk ID: {chunk.id}")
    print(f"Document ID: {chunk.document_id}")
    print(f"Similarity Score: {score:.4f}")
    print("Text:")
    print(chunk.text)