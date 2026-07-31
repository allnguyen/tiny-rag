# TinyRAG Benchmark v1

## Overview

TinyRAG Benchmark v1 is a manually curated retrieval evaluation dataset designed for the TinyRAG project.

Rather than evaluating a language model's generated responses, this benchmark evaluates the retrieval stage of a Retrieval-Augmented Generation (RAG) pipeline.

The benchmark consists of **information needs**, realistic **user query variations**, and manually assigned **ground-truth relevant chunks**. These labels allow retrieval algorithms to be compared objectively using standard Information Retrieval (IR) metrics.

---

# Motivation

A RAG system is only as good as its retriever.

Changing an embedding model, chunking strategy, ranking algorithm, or retrieval method should be measured quantitatively rather than judged by intuition.

TinyRAG Benchmark v1 provides a reproducible evaluation dataset for measuring retrieval quality throughout the development of the project.

---

# Benchmark Design

Unlike many beginner RAG tutorials that evaluate a handful of manually written questions, this benchmark is organized around **information needs**.

Each information need represents a concept a user is trying to learn.

Multiple realistic query variations are associated with each information need to evaluate whether the retrieval system is robust to different ways users naturally express the same intent.

For example:

* Information Need

  * Definition of Retrieval-Augmented Generation

* Query Variations

  * What is RAG?
  * Define RAG.
  * Explain Retrieval-Augmented Generation.
  * What does RAG stand for?

All of these queries should retrieve the same supporting evidence.

---

# Ground Truth

Ground-truth relevance labels are assigned manually.

Each benchmark entry contains one or more chunk IDs that correctly answer the associated information need.

Multiple chunks may be considered relevant when they provide complementary or equivalent information.

The benchmark intentionally separates query generation from relevance labeling:

* Query variations are designed to simulate realistic user behavior.
* Relevant chunk labels represent the authoritative evaluation targets.

---

# Evaluation Metrics

TinyRAG currently supports the following retrieval metrics:

* Precision@K
* Recall@K
* Hit Rate@K
* Mean Reciprocal Rank (MRR)
* Discounted Cumulative Gain (DCG)
* Normalized Discounted Cumulative Gain (nDCG)

These metrics evaluate ranking quality without involving language model generation.

---

# Intended Workflow

1. Build or modify the retrieval pipeline.
2. Run every benchmark query.
3. Retrieve the Top-K chunks.
4. Compare retrieved chunk IDs against the manually labeled ground truth.
5. Compute evaluation metrics.
6. Compare results across retrieval strategies.

---

# Project Goals

TinyRAG Benchmark v1 is intended to evaluate experiments involving:

* Different embedding models
* Chunk size and overlap
* BM25 retrieval
* Dense retrieval
* Hybrid search
* Reranking
* Vector database implementations
* Future agentic retrieval workflows

---

# Future Improvements

Potential future versions of the benchmark may include:

* Larger document collections
* Multiple corpora
* Difficulty ratings
* Query categories
* Graded relevance labels
* Multilingual queries
* Multi-hop retrieval tasks
* Agentic retrieval evaluation

---

# License

This benchmark is intended for educational and research purposes as part of the TinyRAG project.
