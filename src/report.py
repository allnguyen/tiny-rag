"""
report.py

Generates and saves evaluation reports from query-level results
produced by evaluator.py.
"""

from datetime import datetime
from pathlib import Path

import pandas as pd

from config import EVALUATION_REPORTS_PATH

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

    return pd.DataFrame(results)


# =====================================================================
# Level 1 — Overall Performance
# =====================================================================

def overall_performance(
    results: list[dict],
) -> pd.Series:

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

    df = results_to_dataframe(results)

    if df.empty:
        return pd.DataFrame()

    return df[
        df["hit_rate"] == 0
    ].copy()


# =====================================================================
# Build Complete Report
# =====================================================================

def build_report(
    results: list[dict],
) -> str:

    df = results_to_dataframe(results)

    if df.empty:
        return "No evaluation results available."

    lines = []

    # ================================================================
    # Header
    # ================================================================

    lines.append("# TinyRAG Evaluation Report")
    lines.append("")

    lines.append(
        f"Generated: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    lines.append("")
    lines.append(f"Queries evaluated: {len(df)}")
    lines.append("")

    # ================================================================
    # Overall Performance
    # ================================================================

    metrics = overall_performance(results)

    lines.append("## Overall Performance")
    lines.append("")

    lines.append(
        f"- Precision@K: {metrics['precision']:.4f}"
    )

    lines.append(
        f"- Recall@K: {metrics['recall']:.4f}"
    )

    lines.append(
        f"- MRR: {metrics['mrr']:.4f}"
    )

    lines.append(
        f"- nDCG@K: {metrics['ndcg']:.4f}"
    )

    lines.append(
        f"- Hit Rate@K: {metrics['hit_rate']:.4f}"
    )

    lines.append("")

    # ================================================================
    # Performance by Information Need
    # ================================================================

    grouped = performance_by_information_need(results)

    lines.append("## Performance by Information Need")
    lines.append("")

    if grouped.empty:

        lines.append("No information-need results available.")

    else:

        lines.append(
            grouped.to_markdown(
                index=False,
                floatfmt=".4f",
            )
        )

    lines.append("")

    # ================================================================
    # Query-Level Failures
    # ================================================================

    failures = query_failures(results)

    lines.append("## Query-Level Retrieval Failures")
    lines.append("")

    if failures.empty:

        lines.append("No retrieval failures found.")

    else:

        for _, row in failures.iterrows():

            lines.append(
                f"### Benchmark ID: {row['benchmark_id']}"
            )

            lines.append("")

            lines.append(
                f"**Information Need:** "
                f"{row['information_need']}"
            )

            lines.append("")

            lines.append(
                f"**Query:** {row['query']}"
            )

            lines.append("")

            lines.append("**Expected:**")

            lines.append(
                f"`{row['actual']}`"
            )

            lines.append("")

            lines.append("**Retrieved:**")

            lines.append(
                f"`{row['predicted']}`"
            )

            lines.append("")

            lines.append("**Metrics:**")

            lines.append(
                f"- Precision@K: {row['precision']:.4f}"
            )

            lines.append(
                f"- Recall@K: {row['recall']:.4f}"
            )

            lines.append(
                f"- MRR: {row['mrr']:.4f}"
            )

            lines.append(
                f"- nDCG@K: {row['ndcg']:.4f}"
            )

            lines.append(
                f"- Hit Rate@K: {row['hit_rate']:.4f}"
            )

            lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


# =====================================================================
# Save Report
# =====================================================================

def save_report(
report_text: str,
) -> Path:


# Save the evaluation report as a timestamped Markdown file.

    EVALUATION_REPORTS_PATH.mkdir(
    parents=True,
    exist_ok=True,
    )

    timestamp = datetime.now().strftime(
    "%Y-%m-%d_%H-%M-%S"
    )

    report_path = (
    EVALUATION_REPORTS_PATH
    / f"evaluation_report_{timestamp}.md"
    )

    report_path.write_text(
        report_text,
        encoding="utf-8",
    )

    return report_path




# =====================================================================
# Generate Complete Report
# =====================================================================

def generate_report(
    results: list[dict],
) -> None:

    report_text = build_report(results)

    # Print to terminal
    print()
    print(report_text)

    # Save to evaluation_reports/
    report_path = save_report(report_text)

    print()
    print(
        f"Report saved to:\n{report_path}"
    )