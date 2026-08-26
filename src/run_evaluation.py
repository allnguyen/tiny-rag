"""
run_evaluation.py

Entry point for running TinyRAG Benchmark v1.
"""

import json

from pipeline import build_retrieval_system
from evaluator import evaluate
from report import generate_report


# ============================================================
# Load benchmark
# ============================================================

with open(
    r"C:\Users\allan\Projects\experiments\tiny-rag\src\benchmark\benchmark_v1.json",
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
# Generate report
# ============================================================

generate_report(results)