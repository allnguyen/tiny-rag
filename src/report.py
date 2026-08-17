# Load benchmark_v1.json
"""
report.py

Generates an evaluation report from query-level results
produced by evaluator.py.

Responsibilities:
    - Aggregate overall retrieval performance
    - Aggregate performance by information need
    - Identify query-level retrieval failures
    - Display evaluation results

This module does NOT:
    - Perform retrieval
    - Generate embeddings
    - Calculate individual retrieval metrics
    - Modify benchmark labels

The evaluator produces the raw results.
The report analyzes those results.
"""

import pandas as pd


# =====================================================================
# Configuration
# =====================================================================

METRICS = [
    "precision",
    "recall",
    "mrr",
    "ndcg",
    "hit_rate",
]


# =====================================================================
# Convert Results → DataFrame
# =====================================================================

def results_to_dataframe(results: list[dict]) -> pd.DataFrame:
    """
    Convert query-level evaluation results into a pandas DataFrame.

    Args:
        results:
            Output returned by evaluator.evaluate().

    Returns:
        DataFrame containing one row per evaluated query.
    """

    return pd.DataFrame(results)


# =====================================================================
# Level 1 — Overall Performance
# =====================================================================

def overall_performance(
    results: list[dict],
) -> pd.Series:
    """
    Calculate average retrieval performance across
    the entire benchmark.

    Returns:
        Series containing the mean value for each metric.
    """

    df = results_to_dataframe(results)

    if df.empty:
        return pd.Series(dtype=float)

    return df[METRICS].mean()


# =====================================================================
# Level 2 — Performance by Information Need
# =====================================================================

def performance_by_information_need(
    results: list[dict],
) -> pd.DataFrame:
    """
    Calculate average retrieval performance for each
    information need.

    Returns:
        DataFrame containing one row per information need.
    """

    df = results_to_dataframe(results)

    if df.empty:
        return pd.DataFrame()

    return (
        df
        .groupby("information_need")[METRICS]
        .mean()
        .reset_index()
    )


# =====================================================================
# Level 3 — Query-Level Failure Analysis
# =====================================================================

def query_failures(
    results: list[dict],
) -> pd.DataFrame:
    """
    Identify poorly performing queries.

    A query is considered a failure when:
        - Recall@K == 0
        OR
        - Hit Rate@K == 0

    Returns:
        DataFrame containing failed queries.
    """

    df = results_to_dataframe(results)

    if df.empty:
        return pd.DataFrame()

    failures = df[
        (df["recall"] == 0)
        |
        (df["hit_rate"] == 0)
    ].copy()

    return failures


# =====================================================================
# Print Level 1 — Overall Performance
# =====================================================================

def print_overall_performance(
    results: list[dict],
) -> None:
    """
    Print overall benchmark performance.
    """

    df = results_to_dataframe(results)

    if df.empty:
        print("No evaluation results available.")
        return

    metrics = overall_performance(results)

    print("\n")
    print("=" * 60)
    print("TinyRAG Evaluation Report")
    print("=" * 60)

    print(f"\nQueries evaluated: {len(df)}")

    print("\nOverall Performance")
    print("-" * 60)

    print(f"Precision@K:  {metrics['precision']:.4f}")
    print(f"Recall@K:     {metrics['recall']:.4f}")
    print(f"MRR:          {metrics['mrr']:.4f}")
    print(f"nDCG@K:       {metrics['ndcg']:.4f}")
    print(f"Hit Rate@K:   {metrics['hit_rate']:.4f}")


# =====================================================================
# Print Level 2 — Performance by Information Need
# =====================================================================

def print_information_need_performance(
    results: list[dict],
) -> None:
    """
    Print retrieval performance grouped by information need.
    """

    grouped = performance_by_information_need(results)

    if grouped.empty:
        print("\nNo information-need results available.")
        return

    print("\n")
    print("=" * 60)
    print("Performance by Information Need")
    print("=" * 60)

    print()

    print(
        grouped.to_string(
            index=False,
            float_format=lambda value: f"{value:.4f}",
        )
    )


# =====================================================================
# Print Level 3 — Query-Level Failures
# =====================================================================

def print_query_failures(
    results: list[dict],
) -> None:
    """
    Print queries for which retrieval failed to retrieve
    any relevant chunk.
    """

    failures = query_failures(results)

    print("\n")
    print("=" * 60)
    print("Query-Level Retrieval Failures")
    print("=" * 60)

    if failures.empty:
        print("\nNo retrieval failures found.")
        return

    for index, row in failures.iterrows():

        print("\n")
        print(f"Benchmark ID: {row['benchmark_id']}")
        print(f"Information Need: {row['information_need']}")
        print(f"Query: {row['query']}")

        print(f"\nExpected:")
        print(row["actual"])

        print(f"\nRetrieved:")
        print(row["predicted"])

        print("\nMetrics:")
        print(f"Precision@K: {row['precision']:.4f}")
        print(f"Recall@K:    {row['recall']:.4f}")
        print(f"MRR:         {row['mrr']:.4f}")
        print(f"nDCG@K:      {row['ndcg']:.4f}")
        print(f"Hit Rate@K:  {row['hit_rate']:.4f}")

        print("-" * 60)


# =====================================================================
# Generate Complete Report
# =====================================================================

def generate_report(
    results: list[dict],
) -> None:
    """
    Generate the complete TinyRAG evaluation report.

    Includes:
        Level 1 — Overall performance
        Level 2 — Performance by information need
        Level 3 — Query-level failures
    """

    print_overall_performance(results)

    print_information_need_performance(results)

    print_query_failures(results)