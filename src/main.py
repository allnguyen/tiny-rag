"""
main.py

Entry point for the tiny RAG retrieval system.

Pipeline:

1. Load documents from disk
2. Split documents into retrievable chunks
3. Generate embeddings for each chunk
4. Initialize semantic retriever
5. Retrieve most relevant chunks
6. Display retrieval results
"""

from config import DOCUMENTS_PATH
from loader import loader_function
from chunker import Chunker
from embedding import EmbeddingGenerator
from pipeline import build_retrieval_system


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

embedding_generator = EmbeddingGenerator()

print("\n==============================")
print("Generating Chunk Embeddings")
print("==============================")


for chunk in all_chunks:
    chunk.embedding = embedding_generator.generate(
        chunk.text
    )


print(f"Embedded {len(all_chunks)} chunks.")

# ====================================
# 4. Initialize Retriever
# ====================================

retrieval_system = build_retrieval_system()


# ====================================
# 5. User Query
# ====================================

user_query = input("\nEnter your query: ")

print("\n==============================")
print("Search Query")
print("==============================")

print(user_query)



# ====================================
# 6. Retrieve relevant chunks
# ====================================

results = retrieval_system.search(
    user_query,
    top_k=3,
)


# ====================================
# 7. Display results
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