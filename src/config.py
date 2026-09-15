"""
config.py

Central location for project configuration.
"""

from pathlib import Path


# ============================================================
# Project Paths
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCUMENTS_PATH = PROJECT_ROOT / "documents"

BENCHMARKS_PATH = (
    PROJECT_ROOT / "src" / "benchmark"
)

EVALUATION_REPORTS_PATH = (
    PROJECT_ROOT / "evaluation_reports"
)


# ============================================================
# Active Benchmark
# ============================================================

BENCHMARK_PATH = (
    BENCHMARKS_PATH / "benchmark_v2.json"
)


# ============================================================
# Ollama Configuration
# ============================================================

OLLAMA_URL = "http://localhost:11434/api/embed"

EMBEDDING_MODEL = "nomic-embed-text"

EMBEDDING_DIMENSIONS = None

# =============================================================
# Reranking configuration
# =============================================================

RERANKER_MODEL = (
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

RERANKER_CANDIDATE_K = 10