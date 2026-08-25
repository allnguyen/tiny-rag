import json

from evaluator import evaluate
from report import generate_report

# Import whatever you currently use to construct
# your documents, chunks, embeddings, and retriever.


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
# Initialize retrieval system
# ============================================================

retrieval_system = Retriever(
    chunks,
    embedding_generator,
)


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