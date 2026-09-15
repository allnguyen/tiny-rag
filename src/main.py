"""
main.py

Entry point for the tiny RAG retrieval system.

Responsibilities:
    - Build the retrieval system
    - Accept user queries
    - Display retrieval results

"""

from pipeline import build_retrieval_system


# ====================================
# Initialize Retriever
# ====================================

retrieval_system = build_retrieval_system()


# ====================================
# Interactive Query Loop
# ====================================

print("\n==============================")
print("TinyRAG Ready")
print("==============================")

print("Enter a query to search the corpus.")
print("Type 'exit' or 'quit' to stop.")


while True:

    user_query = input("\nWhat is your query? ").strip()

    # Exit condition
    if user_query.lower() in {"exit", "quit"}:
        print("\nExiting TinyRAG.")
        break

    # Ignore empty queries
    if not user_query:
        continue


    # Retrieve relevant chunks
    results = retrieval_system.search(
        user_query,
        top_k=3,
    )

    # Display results
    print("\n==============================")
    print("Retrieval Results")
    print("==============================")


    for rank, (chunk, score) in enumerate(results, start=1):

        print(f"\nRank {rank}")
        print(f"Chunk ID: {chunk.id}")
        print(f"Document ID: {chunk.document_id}")
        print(f"Reranker Score: {score:.4f}")
        print("Text:")
        print(chunk.text)