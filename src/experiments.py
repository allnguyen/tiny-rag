from pipeline import build_retrieval_system

retrieval_system = build_retrieval_system()

query = "Why should we use Retrieval-Augmented Generation?"

dense_candidates, reranked_results = (
    retrieval_system.search_with_diagnostics(query)
)

print("\n==============================")
print("QUERY")
print("==============================")
print(query)

print("\n==============================")
print("DENSE TOP 10")
print("==============================")

for rank, (chunk, score) in enumerate(dense_candidates, start=1):
    print(f"{rank}. {chunk.id} | {score:.4f}")

print("\n==============================")
print("RERANKED TOP 3")
print("==============================")

for rank, (chunk, score) in enumerate(reranked_results, start=1):
    print(f"{rank}. {chunk.id} | {score:.4f}")