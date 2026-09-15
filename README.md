# TinyRAG

TinyRAG is a small **Retrieval-Augmented Generation (RAG) learning system** built from first principles.

The goal is to understand retrieval systems by implementing their core mechanics directly, measuring their behavior, and comparing different retrieval strategies.

---

## Current Objective

The current phase of TinyRAG is **retrieval evaluation**.

The project currently includes:

* A document corpus
* Document loading
* Sentence-based chunking
* Stable document and chunk IDs
* Embedding generation
* A dense semantic retriever
* A labeled **Benchmark v1**
* Retrieval evaluation metrics
* An evaluator
* A reporting layer

The immediate goal is to connect these components into one reliable, end-to-end evaluation pipeline.

Once the baseline is working, retrieval strategies will become replaceable so that **Dense Retrieval, BM25, Hybrid Retrieval, and later Reranking** can be evaluated using the same benchmark and evaluation framework.

---

## Architecture

The current retrieval pipeline is:

```text
Documents
    |
    v
Document Loader
    |
    v
Documents
    |
    v
Chunker
    |
    v
Chunks
    |
    v
Embedding Generator
    |
    v
Embedded Chunks
    |
    v
Dense Retriever
    |
    +---- Query
            |
            v
      Query Embedding
            |
            v
      Cosine Similarity
            |
            v
       Ranked Chunks
            |
            v
           Top-K
```

### Dense Retrieval Baseline

The current baseline uses dense semantic retrieval:

```text
Query
  |
  v
Query Embedding
  |
  v
Compare against chunk embeddings
  |
  v
Cosine Similarity
  |
  v
Sort by similarity
  |
  v
Return Top-K chunks
```

This intentionally implements the core retrieval mechanics directly rather than hiding them behind a retrieval framework.

---

# Corpus

The current corpus covers concepts including:

* Information Retrieval
* Embeddings
* Cosine Similarity
* BM25
* Dense Retrieval
* Vector Databases
* Chunking
* Reranking
* Hybrid Search
* RAG Pipeline

### Current Corpus Size

The latest successful run reported:

```text
Documents loaded:       11
Chunks created:         70
Chunk embeddings:       70
```

Stable chunk IDs such as `010-001` are used as the units referenced by Benchmark v1 ground-truth labels.

---

# Benchmark v1

Benchmark v1 provides the ground truth used to evaluate retrieval quality.

Each benchmark entry contains:

```json
{
  "id": 40,
  "information_need": "Definition of vector databases",
  "description": "The user wants to understand what a vector database is.",
  "queries": [
    "What is a vector database?",
    "Define vector database."
  ],
  "relevant_chunks": [
    "006-001",
    "006-002"
  ]
}
```

## Benchmark Structure

### `information_need`

Identifies the underlying concept or information need.

### `description`

Describes what the user is trying to understand or retrieve.

### `queries`

Contains multiple ways of expressing the same information need.

### `relevant_chunks`

Contains the labeled ground-truth chunk IDs that are considered relevant to the information need.

Benchmark v1 has been labeled and reviewed for consistency.

The benchmark is designed to distinguish **information needs** from individual query wording so that multiple query formulations can be evaluated against the same ground truth.

---

# Evaluation

TinyRAG evaluates retrieval results against Benchmark v1.

The evaluation layer currently implements:

* Precision@K
* Recall@K
* Mean Reciprocal Rank (MRR)
* DCG
* nDCG@K
* Hit Rate@K

The evaluator compares the benchmark ground truth against the chunks returned by the retrieval system.

Conceptually:

```text
Actual
    =
benchmark["relevant_chunks"]

Predicted
    =
retrieval_system.search(query, top_k)
```

The evaluator runs every benchmark query and produces one result record per query.

## Query-Level Evaluation Record

Each result should contain:

```text
benchmark_id
information_need
query
actual
predicted
precision
recall
mrr
ndcg
hit_rate
```

---

# Reporting

`report.py` is responsible for aggregating evaluation results into progressively more useful views.

### Level 1 — Overall Performance

Overall retrieval performance across the benchmark.

```text
Precision@K
Recall@K
MRR
nDCG@K
Hit Rate@K
```

### Level 2 — Performance by Information Need

Identify which concepts the retrieval system handles well or poorly.

### Level 3 — Query-Level Failures

Inspect individual queries where retrieval failed or performed poorly.

### Level 4 — Retrieval System Comparison

This will be added later to compare different retrieval strategies using the same benchmark.

```text
Dense Retrieval
      |
      +------+
             |
BM25 --------+----> Evaluation ----> Comparison
             |
Hybrid ------+
```

---

# Current Status

## Completed

* [x] Document loader
* [x] Document objects
* [x] Sentence-based chunking
* [x] Stable document/chunk IDs
* [x] Chunk embeddings
* [x] Dense semantic retrieval
* [x] Cosine similarity
* [x] Ranked Top-K retrieval
* [x] Benchmark v1 design
* [x] Benchmark v1 labeling
* [x] Benchmark consistency review
* [x] Precision@K
* [x] Recall@K
* [x] MRR
* [x] DCG
* [x] nDCG@K
* [x] Hit Rate@K
* [x] Evaluator design
* [x] Report design

## Current Integration Work

The individual components exist, but the evaluation pipeline is not yet cleanly executable end-to-end.

Current integration issues include:

* `main.py` creates a retriever but later calls `retrieval_system.search(...)`.
* `evaluator.py` is duplicated in the current working material.
* `evaluator.py` is missing a comma after `"information_need": entry["information_need"]`.
* The report runner references chunks and `embedding_generator` without constructing them.
* `report.py` defines reporting functions but does not itself build a retrieval system or run the evaluator.
* Corpus and retrieval construction currently live inside `main.py`, making reuse from `report.py` awkward.

These are **integration issues rather than failures of the underlying retrieval or evaluation design**.

---

# Immediate Milestone

The next milestone is:

> **Run Benchmark v1 end-to-end against the current dense retriever and produce a trustworthy baseline report.**

The desired flow is:

```text
benchmark_v1.json
        |
        v
Retrieval System
        |
        v
evaluator.py
        |
        v
Query-Level Results
        |
        v
report.py
        |
        v
TinyRAG Evaluation Report
```

New retrieval strategies will only be implemented after this baseline evaluation pipeline works reliably.

---

# Future Experiments

## 1. BM25

Implement a lexical retriever using the same conceptual interface:

```python
search(query, top_k)
```

Evaluate BM25 against the exact same Benchmark v1.

This will allow direct comparison between:

```text
Dense Retrieval
vs.
BM25
```

---

## 2. Hybrid Retrieval

Combine lexical and semantic retrieval.

The goal is to compare:

```text
Dense
BM25
Hybrid
```

using the same benchmark and metrics.

This will make it possible to investigate questions such as:

* When does semantic retrieval perform better?
* When does lexical retrieval perform better?
* Does combining the two improve overall retrieval quality?
* Which information needs benefit most from hybrid retrieval?

---

## 3. Reranking

A later retrieval pipeline may introduce a reranking stage:

```text
First-Stage Retrieval
        |
        v
Candidate Set
        |
        v
Reranker
        |
        v
Final Ranking
```

This will allow evaluation of the tradeoff between retrieval quality and additional computation.

---

## 4. Retrieval Latency

Quality will eventually be evaluated alongside retrieval latency.

Example:

| Retriever | Quality | Latency |
| --------- | ------: | ------: |
| Dense     |     ... |     ... |
| BM25      |     ... |     ... |
| Hybrid    |     ... |     ... |
| Reranked  |     ... |     ... |

The goal is to understand the tradeoff between **retrieval quality and system cost/latency**, rather than optimizing for a single metric.

---

# LLM Generation

Once retrieval is stable, an LLM generation layer can be added:

```text
User Query
    |
    v
Retriever
    |
    v
Relevant Chunks
    |
    v
Context
    |
    v
LLM
    |
    v
Answer
```

The focus will remain on understanding the relationship between retrieval quality and downstream answer quality.

---

# Advanced / Agentic RAG

Agentic and multi-step retrieval will come **after the underlying retrieval pipeline is understood and evaluated**.

A possible future direction is:

```text
User Query
    |
    v
Query Analysis
    |
    v
Query Decomposition
    |
    +----------+----------+
    |                     |
    v                     v
Sub-query A           Sub-query B
    |                     |
    v                     v
Retrieve               Retrieve
    |                     |
    +----------+----------+
               |
               v
        Combined Evidence
               |
               v
          Final Answer
```

The goal is to understand how retrieval behaves when a system must perform multiple retrieval steps rather than treating agentic RAG as a black box.

---

# Project Philosophy

TinyRAG is intentionally small.

The purpose is not to build a production-scale RAG platform. The purpose is to make the mechanics of retrieval **visible, measurable, and replaceable**.

The project is designed to build an understanding of:

* What a corpus is
* How documents are represented
* What chunks are
* What embeddings represent
* How similarity works
* How retrieval produces a ranking
* How relevance labels define ground truth
* Why retrieval systems fail
* How retrieval quality is measured
* How different retrieval strategies behave
* How retrieval quality trades off against latency and complexity

The guiding principle is:

> **Understand the retrieval system before hiding it behind a framework.**

---

# Roadmap

```text
Corpus
   |
   v
Chunking
   |
   v
Embeddings
   |
   v
Dense Retrieval
   |
   v
Benchmark v1
   |
   v
Evaluation Metrics
   |
   v
[ CURRENT: Integration ]
   |
   v
Baseline Report
   |
   v
BM25
   |
   v
Hybrid Retrieval
   |
   v
Reranking
   |
   v
LLM / RAG Generation
   |
   v
Advanced / Agentic RAG
```

---

# Current Goal

**Build a reliable retrieval evaluation baseline before adding more complexity.**

The immediate question TinyRAG is trying to answer is:

> **How well does a simple dense retrieval system retrieve the information a user actually needs, and where does it fail?**

Once that baseline is trustworthy, more advanced retrieval strategies can be added and evaluated systematically.
