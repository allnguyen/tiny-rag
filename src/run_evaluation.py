"""
run_evaluation.py

Entry point for running TinyRAG Benchmark v2.
"""

import json

from pipeline import build_retrieval_system
from evaluator import evaluate
from report import generate_report
from config import BENCHMARK_PATH

# ============================================================
# Load benchmark
# ============================================================

with open(
    BENCHMARK_PATH,
    "r",
    encoding="utf-8",
) as file:

    benchmark = json.load(file)


# ============================================================
# Build retrieval system
# ============================================================

retrieval_system = build_retrieval_system()


# ============================================================
# Run evaluation
# ============================================================

results = evaluate(
    retrieval_system,
    benchmark,
    k=3,
)


# ============================================================
# Generate and save report
# ============================================================

generate_report(results)