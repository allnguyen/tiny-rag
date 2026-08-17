"""
evaluator.py

"""
from evaluation import (
    precision_at_k,
    recall_at_k,
    mean_reciprocal_rank,
    ndcg_at_k,
    hit_rate_at_k,
)


def evaluate(retrieval_system, benchmark, k):

    results = []

    for entry in benchmark:

        # Ground-truth relevant chunks for this information need
        actual = entry["relevant_chunks"]

        for query in entry["queries"]:

            # Run the benchmark query through the retrieval system
            retrieved = retrieval_system.search(
                query,
                top_k=k
            )

            # Extract ranked chunk IDs from retrieval result
            predicted = [
                chunk.id 
                for chunk, score in retrieved
            ]
     
            # Calculate metrics
            precision = precision_at_k(
                actual,
                predicted,
                k
            )

            recall = recall_at_k(
                actual,
                predicted,
                k
            )

            mrr = mean_reciprocal_rank(
                actual,
                predicted
            )

            ndcg = ndcg_at_k(
                actual,
                predicted,
                k
            )

            hit_rate = hit_rate_at_k(
                actual,
                predicted,
                k
            )

            # Store query-level evaluation results



            results.append({
                "benchmark_id": entry["id"],
                "query": query,
                "actual": actual,
                "predicted": predicted,
                "precision": precision,
                "recall": recall,
                "mrr": mrr,
                "ndcg": ndcg,
                "hit_rate": hit_rate
            })

    return results