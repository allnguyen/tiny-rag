# Tiny RAG — Building a Retrieval System from First Principles

A lightweight Retrieval-Augmented Generation (RAG) learning project focused on understanding the core mechanics of modern information retrieval systems without relying on high-level frameworks such as LangChain or LlamaIndex.

Rather than treating RAG as a black box, this project implements each component individually to understand how semantic search works under the hood—from loading documents and generating embeddings to retrieving relevant information using vector similarity.

> **Project Status:** Chunk-based semantic retrieval pipeline complete. Retrieval evaluation and generation pipeline under active development.

---

# Motivation

Modern AI applications increasingly rely on Retrieval-Augmented Generation (RAG) to provide accurate, grounded responses from external knowledge sources. While many tutorials use frameworks that abstract away the underlying retrieval process, this project focuses on implementing the retrieval system from scratch.

The objectives are to:

* Understand dense semantic retrieval from first principles.
* Learn how embeddings represent natural language.
* Build modular software components using sound software engineering principles.
* Gain practical experience with the architecture behind production RAG systems.

---

# Current Features

## Implemented

* ✅ Load a corpus of text documents
* ✅ Represent documents using structured data classes
* ✅ Generate dense embeddings locally with Ollama
* ✅ Compute cosine similarity between embeddings
* ✅ Perform semantic retrieval using brute-force vector search
* ✅ Split documents into sentence-based retrieval chunks
* ✅ Generate embeddings for individual chunks
* ✅ Perform chunk-level semantic retrieval
* ✅ Rank retrieved chunks using cosine similarity
* ✅ Return the Top-K most relevant chunks

## Planned

* ⏳ Vector indexing (uSearch)
* ⏳ Persistent embedding storage
* ⏳ Retrieval evaluation metrics
* ⏳ Hybrid search (BM25 + Dense Retrieval)
* ⏳ Cross-encoder reranking
* ⏳ LLM response generation
* ⏳ Complete Retrieval-Augmented Generation pipeline

---

# High-Level Architecture

```text
                    User Query
                         │
                         ▼
               EmbeddingGenerator
                         │
                         ▼
                 Query Embedding
                         │
                         ▼
                  Retriever.search()
                         │
        ┌────────────────┴────────────────┐
        │                                 │
        ▼                                 ▼
chunk.embedding                 cosine_similarity()
        │                                 │
        └──────────────┬──────────────────┘
                       ▼
             Similarity Scores
                       ▼
              Sort Highest → Lowest
                       ▼
                Return Top-K Chunks


---

# Retrieval Pipeline

The current system executes the following pipeline:

```
Text Documents
      │
      ▼
Document Loader
      │
      ▼
Document Objects
      │
      ▼
Chunker
      │
      ▼
Chunk Objects
      │
      ▼
Embedding Generator 
      │
      ▼
Chunk Embeddings
      │
      ▼
User Query
      │
      ▼
Query Embedding
      │
      ▼
Retriever
      │
      ▼
Cosine Similarity
      │
      ▼
Rank Chunks
      │
      ▼
Top-K Results


The retrieval system currently performs **dense semantic search** using cosine similarity over locally generated embedding vectors.

---

# Project Structure

```text
tiny-rag/
│
├── config.py
├── document.py
├── loader.py
├── chunk.py
├── chunker.py
├── embedding.py
├── similarity.py
├── retriever.py
├── main.py
├── requirements.txt
│
└── documents/
    ├── 001_information_retrieval.txt
    ├── 002_embeddings.txt
    ├── 003_cosine_similarity.txt
    ├── ...
```

---

# Component Overview

## Document

Represents a single document in the corpus.

Stores:

* ID
* Title
* File metadata
* Raw text
* Embedding vector

The `Document` class is intentionally a data container and contains no retrieval logic.

---

## Loader

Reads every text file from the corpus directory and converts each into a `Document` object.

Responsible only for:

* File discovery
* Reading files
* Creating document objects

---
## Chunk

Represents the fundamental retrieval unit within the corpus.

Stores:

Chunk ID
Parent document ID
Chunk text
Embedding vector

Unlike a Document, a Chunk is designed to be retrieved directly by the semantic search pipeline.
---
## Chunker

Transforms a Document into a collection of smaller retrievable units.

Current strategy:

Sentence-based chunking

Future strategies:

Paragraph chunking
Token-based chunking
Semantic chunking

Separating chunking into its own component allows retrieval strategies to evolve independently of the rest of the pipeline.
---
## EmbeddingGenerator

Converts natural language into dense numerical vectors using a locally hosted Ollama embedding model.

Input:

```
Text
```

Output:

```
Embedding Vector
```

This component encapsulates all interaction with Ollama.

---

## Similarity

Provides reusable mathematical utilities for comparing embedding vectors.

Currently implements:

* Cosine Similarity

The module is intentionally independent of the retrieval system.

---

## Retriever

Performs semantic search across the document corpus.

Responsibilities:

* Compare query embedding against every chunk embedding
* Compute similarity scores
* Rank chunks by semantic similarity
* Return the Top-K most relevant chunks

The retriever assumes embeddings already exist and does not generate them.

---

## Main

Coordinates the complete retrieval pipeline.

Responsibilities:

1. Load documents
2. Generate embeddings
3. Embed user query
4. Retrieve chunks
5. Display ranked results

Business logic remains inside dedicated modules.

---

# Technologies

* Python
* Ollama
* nomic-embed-text
* Dense Vector Embeddings
* Cosine Similarity
* Semantic Search
* Retrieval-Augmented Generation (RAG)

Future:

* uSearch
* Hybrid Retrieval
* Cross-Encoder Reranking

---

# Design Principles

This project emphasizes modular software architecture in addition to machine learning concepts.

Each module has a single responsibility:

| Component          | Responsibility                 |
| ------------------ | -------------------------------|
| Document           | Store document data            |
| Loader             | Read corpus from disk          |
| Chunk              | Stores retrievable unit        |
| Chunker            | Transform Document into Chunks |
| EmbeddingGenerator | Generate embeddings            |
| Similarity         | Compare vectors                |
| Retriever          | Perform semantic retrieval     |
| Main               | Orchestrate the pipeline       |

This separation makes components independently testable and replaceable. For example, the current brute-force retrieval implementation can later be replaced with a vector index (uSearch) without changing the rest of the system.

---

# Current Limitations

This project intentionally prioritizes understanding over optimization.

Current limitations include:

* Current chunking strategy is sentence-based and does not preserve multi-sentence context.
* Chunk embeddings are regenerated on every execution.
* Retrieval uses brute-force linear search (O(N)).
* No persistent vector index has been implemented.
* No reranking stage.
* No automated retrieval evaluation metrics yet.
* No response generation with an LLM.

These limitations are intentional and will be addressed incrementally throughout future development.

---

# Example Output

==============================
Retrieval Results
==============================

Query:
What is BM25?

Rank 1
Chunk ID: 004-002
Document ID: 004
Similarity Score: 0.9412

BM25 is a lexical ranking algorithm commonly used
in information retrieval systems...

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/tiny-rag.git

cd tiny-rag
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Install the embedding model:

```bash
ollama pull nomic-embed-text
```

Run the project:

```bash
python main.py
```

---

# Roadmap

## Phase 1 — Retrieval Foundations ✅

* [x] Document loading
* [x] Structured document representation
* [x] Local embedding generation
* [x] Cosine similarity
* [x] Semantic retrieval
* [x] Top-K ranking

## Phase 2 — Retrieval Improvements

* [x] Sentence-based chunking
* [x] Chunk embeddings
* [x] Chunk-level retrieval
* [ ] Persistent embedding storage
* [ ] Vector indexing (uSearch)
* [ ] Retrieval benchmarking
* [ ] Recall@K
* [ ] Mean Reciprocal Rank
* [ ] Precision@K
* [ ] NDCG
* [ ] Latency measurement

## Phase 3 — Production-Style RAG

* [ ] Hybrid Retrieval (BM25 + Dense)
* [ ] Cross-Encoder Reranking
* [ ] Prompt construction
* [ ] LLM response generation
* [ ] End-to-end Retrieval-Augmented Generation pipeline

---

# What I'm Learning

This project has helped me develop a practical understanding of:

* Information Retrieval (IR)
* Semantic Search
* Dense Embeddings
* Vector Similarity
* Retrieval-Augmented Generation (RAG)
* Software architecture for AI systems
* Modular component design
* Retrieval system evaluation

More importantly, it has given me an appreciation for how production retrieval systems are engineered—from the underlying mathematics of vector similarity to the software design decisions that make complex AI systems maintainable and extensible.

---

# License

This project is intended for educational and learning purposes.
