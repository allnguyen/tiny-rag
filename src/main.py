"""
main.py

Entry point for the tiny RAG retrieval system. 

This file coordinates the pipeline:

1. Load documents
2. Generate document embeddings
3. Accepts user query
4. Generate query embedding
5. Retrieve most relevant documents
6. Display results
"""



from config import DOCUMENTS_PATH
from loader import loader_function
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
print("Corpus Summary")
print("================================")

print(f"Documents loaded: {len(documents)}")

for document in documents:
    print(f"{document.id}: {document.title}")


# =====================================
# 2. Generate document embeddings
# =====================================


print("\n==============================")
print("Generating Embeddings")
print("================================")



generator = EmbeddingGenerator()



for document in documents:
    document.embedding = generator.generate(
        document.text
    )

    print(f"\n✓ {document.title}")
    print(
        f"  Dimensions: {len(document.embedding)}"
    )
    print(
        f"  First 5 values: {document.embedding[:5]}"
    )


print("\nDocument embeddings complete.")



# =======================================
# 3. Initialize retriever 
# =======================================

retriever = Retriever(documents) 


# =======================================
# 4. User query
# =======================================

user_query = "What is BM25?"



print("\n==============================")
print("Search Query")
print("==============================")

print(user_query)


# =====================================
# 5. Generate query embedding
# =====================================

query_embedding = generator.generate(
    user_query
)

# Debug to confirm Document embeddings, query embeddings, work and have same dimension 

print("\nTesting query embedding...")
print(f"Query dimensions: {len(query_embedding)}")
print(f"First 5 values: {query_embedding[:5]}")

# ===================================
# 6. Retrieve documents
# ===================================

results = retriever.search(
    query_embedding,
    top_k=3
)


# ===================================
# 7. Display results
# ===================================

print("\n==============================")
print("Retrieval Results")
print("==============================")


for rank, (document, score) in enumerate(results, start=1):

    print(f"\nRank {rank}")
    print(f"Document: {document.title}")
    print(f"Similarity Score: {score:.4f}")