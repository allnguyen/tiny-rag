from config import DOCUMENTS_PATH
from loader import loader_function
from embedding import EmbeddingGenerator
from retriever import Retriever
from similarity import cosine_similarity


# ==============================
# 1. Load documents
# ==============================

documents = loader_function(DOCUMENTS_PATH)


# ==============================
# 2. Summarize corpus
# ==============================

print("\n==============================")
print("Corpus Summary")
print("==============================")

print(f"Documents loaded: {len(documents)}")

if documents:
    print("\nDocuments:")
    for doc in documents:
        print(f"  {doc.id}: {doc.title}")
else:
    print("No documents found.")
    exit()


# ==============================
# 3. Initialize embedding generator
# ==============================

generator = EmbeddingGenerator()


# ==============================
# 4. Generate embeddings
# ==============================

print("\n==============================")
print("Generating Embeddings")
print("==============================")


for document in documents:
    document.embedding = generator.generate(document.text)

    print(f"\n✓ {document.title}")
    print(f"  Embedding dimensions: {len(document.embedding)}")
    print(f"  First 5 values: {document.embedding[:5]}")


# ==============================
# 5. Final summary
# ==============================

print("\n==============================")
print("Embedding Generation Complete")
print("==============================")

print(f"Successfully embedded {len(documents)} documents.")


# =======================
# Retreival
# =======================

retriever = Retriever(documents)
results = retriever.search(query_embedding)
query_embedding = generator.generate(user_query)