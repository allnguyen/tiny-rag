TinyRAG

TinyRAG is a small Retrieval-Augmented Generation (RAG) learning system
built from first principles.

The goal is to understand retrieval systems by implementing their core
mechanics directly, measuring their behavior, and then comparing
retrieval strategies.

Current objective

The current phase is retrieval evaluation.

The project now has a corpus, chunking, embeddings, a dense retriever, a
labeled Benchmark v1, retrieval metrics, an evaluator, and a reporting
layer. The immediate goal is to connect these pieces into one reliable
end-to-end evaluation pipeline.

Current architecture

Documents
    |
    v
Loader
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
EmbeddingGenerator
    |
    v
Embedded Chunks
    |
    v
Retriever
    |
    +---- query
    |
    v
Query Embedding
    |
    v
Cosine Similarity
    |
    v
Ranked Chunks

The current baseline is a dense semantic retriever:

query
  -> embedding
  -> compare against every chunk embedding
  -> cosine similarity
  -> sort
  -> top-K

Corpus

The corpus covers concepts including:

Information Retrieval

Embeddings

Cosine Similarity

BM25

Dense Retrieval

Vector Databases

Chunking

Reranking

Hybrid Search

RAG Pipeline

The latest run reported:

11 documents loaded

70 chunks created

70 chunk embeddings generated

Chunk IDs such as 010-001 are the units used by Benchmark v1
ground-truth labels.

Benchmark v1

Each benchmark entry contains:

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

information_need identifies the underlying concept. queries contains
multiple ways of expressing that need. relevant_chunks contains the
labeled ground-truth chunk IDs.

Benchmark v1 has been labeled and reviewed for consistency.

Evaluation

evaluation.py contains:

Precision@K

Recall@K

Mean Reciprocal Rank (MRR)

DCG

nDCG@K

Hit Rate@K

The evaluator compares:

actual
    =
benchmark["relevant_chunks"]

predicted
    =
retrieval_system.search(...)[chunk IDs]

evaluator.py runs every benchmark query and returns one result record
per query.

A result should contain:

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

report.py is responsible for:

Level 1: overall performance

Level 2: performance by information need

Level 3: query-level failures

Level 4 comparison between retrieval systems comes later.

Current status

Completed

Document loader

Document objects

Sentence-based chunking

Stable document/chunk IDs

Chunk embeddings

Dense semantic retrieval

Cosine similarity

Ranked top-K retrieval

Benchmark v1 design

Benchmark v1 labeling

Benchmark consistency review

Precision@K

Recall@K

MRR

DCG

nDCG

Hit Rate@K

Evaluator design

Report design

Not yet cleanly integrated

The individual components exist, but the evaluation pipeline is not yet
cleanly executable end-to-end.

Known integration issues in the current pasted code:

main.py creates retriever but later calls
retrieval_system.search(...).

evaluator.py is duplicated in the working material.

evaluator.py is missing a comma after
"information_need": entry["information_need"].

The report runner references chunks and embedding_generator
without constructing them.

report.py defines reporting functions but does not itself build a
retrieval system or run the evaluator.

Corpus/retrieval construction currently lives inside main.py,
making reuse from report.py awkward.

These are integration problems, not a failure of the underlying design.

Immediate milestone

Run Benchmark v1 end-to-end against the current dense retriever and
produce a trustworthy baseline report.

Desired flow:

benchmark_v1.json
        |
        v
retrieval system
        |
        v
evaluator.py
        |
        v
query-level results
        |
        v
report.py
        |
        v
TinyRAG Evaluation Report

Only after this works should new retrieval strategies be implemented.

Future experiments

BM25

Implement a lexical retriever with the same conceptual interface:

search(query, top_k)

Evaluate it against the exact same Benchmark v1.

Hybrid retrieval

Combine BM25 and dense retrieval and compare:

Dense
BM25
Hybrid

Reranking

Later:

first-stage retrieval
        |
candidate set
        |
reranker
        |
final ranking

Latency

Measure retrieval latency alongside quality:

Retriever    Quality    Latency
Dense        ...        ...
BM25         ...        ...
Hybrid       ...        ...
Reranked     ...        ...

LLM generation

After retrieval is stable:

User query
    |
    v
Retriever
    |
    v
Relevant chunks
    |
    v
Context
    |
    v
LLM
    |
    v
Answer

Agentic RAG should come later, after the underlying retrieval pipeline
is understood.

Project philosophy

TinyRAG is intentionally small. Its purpose is to make retrieval
mechanics visible rather than hiding them behind a framework.

The project is intended to teach:

what a corpus is

what chunks are

what embeddings represent

how similarity works

how retrieval produces a ranking

why retrieval fails

how relevance labels define ground truth

how retrieval quality is measured

how retrieval strategies trade off quality and speed

The system is currently at:

Corpus
  -> Chunking
  -> Embeddings
  -> Dense Retrieval
  -> Benchmark v1
  -> Evaluation Metrics
  -> [CURRENT: Integration]
  -> Baseline Report
  -> BM25
  -> Hybrid
  -> Reranking
  -> LLM / RAG generation
  -> Advanced / Agentic RAG