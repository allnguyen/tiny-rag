"""
evaluator.py

Runs the benchmark against a retrieval system and produces
query-level evaluation results.

Responsibilities:
    - Iterate through every benchmark entry
    - Run every benchmark query through the retrieval system
    - Extract predicted chunk IDs
    - Compare predictions against labeled relevant chunks
    - Calculate retrieval metrics
    - Return one result record per query

This module does NOT:
    - Load documents
    - Generate chunk embeddings
    - Generate query embeddings directly
    - Perform retrieval itself
    - Aggregate results into a report

The retrieval system is intentionally passed in so that different
retrieval strategies can be evaluated using the same benchmark.
"""
from evaluation import (
    precision_at_k,
    recall_at_k,
    mean_reciprocal_rank,
    ndcg_at_k,
    hit_rate_at_k,
)


def evaluate(
    retrieval_system, 
    benchmark: list[dict], 
    k: int = 3,
) -> list[dict]:
    """
    Run every benchmark query through the retrieval system
    and calculate retrieval metrics.

    Args:
        retrieval_system:
            Retrieval system implementing:

                search(query, top_k)

        benchmark:
            Loaded TinyRAG Benchmark v1 data.

        k:
            Number of chunks to retrieve and evaluate.

    Returns:
        A list containing one result dictionary per benchmark query.
    """

    results = []

    # ================================================================
    # Run every benchmark entry
    # ================================================================

    for entry in benchmark:

        benchmark_id = entry["id"]
        information_need = entry["information_need"]
        actual = entry["relevant_chunks"]

        for query in entry["queries"]:

            # --------------------------------------------------------
            # 1. Retrieve top-K chunks
            # --------------------------------------------------------

            retrieved = retrieval_system.search(
                query,
                top_k=k,
            )

            # --------------------------------------------------------
            # 2. Extract predicted chunk IDs
            # --------------------------------------------------------

            predicted = [
                chunk.id 
                for chunk, score in retrieved
            ]
     
            # --------------------------------------------------------
            # 3. Calculate evaluation metrics
            # --------------------------------------------------------
            
            precision = precision_at_k(
                actual,
                predicted,
                k,
            )

            recall = recall_at_k(
                actual,
                predicted,
                k,
            )

            mrr = mean_reciprocal_rank(
                actual,
                predicted,
            )

            ndcg = ndcg_at_k(
                actual,
                predicted,
                k,
            )

            hit_rate = hit_rate_at_k(
                actual,
                predicted,
                k,
            )

            # Store query-level evaluation results
            results.append({
                "benchmark_id": benchmark_id,
                "information_need": information_need,
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