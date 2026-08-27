# TinyRAG Evaluation Report 1 — Baseline

**Date:** 2026-08-26  
**System:** TinyRAG  
**Evaluation:** Dense Retrieval Baseline  
**Retrieval:** Embedding-based semantic search using cosine similarity  
**K:** 3  
**Queries Evaluated:** 217

---

## 1. Purpose

This report establishes the first quantitative baseline for the TinyRAG retrieval system.

The goal of this evaluation is not yet to optimize retrieval performance, but to:

- Establish baseline retrieval metrics.
- Identify systematic retrieval failures.
- Determine which information needs are difficult for the current system.
- Understand whether failures are caused by ranking, semantic ambiguity, corpus structure, or other factors.
- Create a reference point for future retrieval experiments.

The baseline will be used to compare future changes to the retrieval system.

---

# 2. System Under Evaluation

The current TinyRAG pipeline:

1. Loads a document corpus.
2. Splits documents into retrievable chunks.
3. Generates embeddings using Ollama.
4. Stores embeddings on chunks.
5. Generates an embedding for each query.
6. Calculates cosine similarity between the query and chunk embeddings.
7. Ranks chunks by similarity.
8. Returns the top-K results.
9. Accepts user queries.
10. Evaluates retrieval against a labeled benchmark.

The evaluation framework calculates:

- Precision@K
- Recall@K
- Mean Reciprocal Rank (MRR)
- nDCG@K
- Hit Rate@K

---

# 3. Benchmark

The evaluation contains:

**217 queries**

The queries are organized by information need and mapped to expected relevant chunks.

The benchmark includes multiple query formulations for the same information need in order to test whether retrieval remains effective when the wording of the query changes.

---

# 4. Overall Baseline Results

| Metric | Score |
|---|---:|
| Precision@3 | 0.3226 |
| Recall@3 | 0.6029 |
| MRR | 0.6575 |
| nDCG@3 | 0.5621 |
| Hit Rate@3 | 0.8479 |

---

## 4.1 Initial Interpretation

The baseline shows that the system is capable of retrieving relevant information, but its ranking quality is considerably weaker than its ability to retrieve something relevant.

The most notable result is the difference between:

- **Hit Rate@3: 0.8479**
- **Precision@3: 0.3226**

The system frequently retrieves a relevant chunk somewhere in the top three results, but the retrieved set often contains irrelevant or less-appropriate chunks.

This suggests that the primary problem is not simply:

> "Can the system find relevant information?"

but increasingly:

> "Can the system identify the most appropriate chunk and rank it highly?"

The MRR score of **0.6575** also indicates that relevant results are often appearing relatively high in the ranking, although not consistently at rank 1.

---

# 5. Performance by Information Need

| Information Need | Precision | Recall | MRR | nDCG | Hit Rate |
|---|---:|---:|---:|---:|---:|
| Applications of RAG | 0.2778 | 0.8333 | 0.8333 | 0.8333 | 0.8333 |
| Characteristics of a good RAG system | 0.3333 | 1.0000 | 0.8000 | 0.8524 | 1.0000 |
| Consumers of food | 0.3333 | 1.0000 | 0.8750 | 0.9077 | 1.0000 |
| Cosine similarity applications | 0.3333 | 0.3333 | 0.3333 | 0.2346 | 1.0000 |
| Cosine similarity formula | 0.3333 | 0.5000 | 0.5000 | 0.3869 | 1.0000 |
| Creators of food | 0.1111 | 0.3333 | 0.1667 | 0.2103 | 0.3333 |
| Definition of BM25 | 0.3333 | 0.3333 | 1.0000 | 0.4693 | 1.0000 |
| Definition of Information Retrieval (IR) | 0.3333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Definition of RAG | 0.3333 | 1.0000 | 0.6190 | 0.7177 | 1.0000 |
| Definition of chunking | 0.3333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Definition of cosine similarity | 0.6667 | 0.6667 | 1.0000 | 0.7654 | 1.0000 |
| Definition of dense retrieval | 0.3333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Definition of embeddings | 0.3333 | 0.5000 | 0.5000 | 0.3869 | 1.0000 |
| Definition of food | 0.3333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Definition of hybrid search | 0.3333 | 1.0000 | 0.7143 | 0.7891 | 1.0000 |
| Definition of reranking | 0.3333 | 0.5000 | 1.0000 | 0.6131 | 1.0000 |
| Definition of vector databases | 0.3333 | 0.3333 | 1.0000 | 0.4693 | 1.0000 |
| Dense retrieval versus BM25 | 0.7222 | 0.5417 | 0.9167 | 0.7654 | 1.0000 |
| Designing chunking strategy | 0.3333 | 0.3333 | 1.0000 | 0.4693 | 1.0000 |
| Goal of Information Retrieval | 0.1667 | 0.5000 | 0.2222 | 0.2936 | 0.5000 |
| How Information Retrieval systems work | 0.2222 | 0.1667 | 0.4259 | 0.2290 | 0.6667 |
| Importance of BM25 | 0.6667 | 0.5000 | 0.5000 | 0.5307 | 1.0000 |
| Importance of Information Retrieval (IR) | 0.2857 | 0.8571 | 0.3095 | 0.4473 | 0.8571 |
| Importance of RAG | 0.1111 | 0.3333 | 0.1389 | 0.1885 | 0.3333 |
| Importance of embeddings | 0.4667 | 0.3500 | 0.9000 | 0.5285 | 1.0000 |
| Importance of food | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Importance of hybrid search in RAG | 0.3333 | 0.5000 | 1.0000 | 0.6131 | 1.0000 |
| Importance of reranking | 0.3333 | 0.3333 | 0.7500 | 0.3827 | 1.0000 |
| Importance of vector databases | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Location of food | 0.3333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Meaning of cosine similarity scores | 0.3333 | 1.0000 | 0.8571 | 0.8946 | 1.0000 |
| Mechanics of dense retrieval | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Mechanics of vector databases | 0.3333 | 0.5000 | 0.5000 | 0.3869 | 1.0000 |
| Origin of embeddings | 0.3333 | 1.0000 | 0.3889 | 0.5436 | 1.0000 |
| RAG architecture | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Reranking methods | 0.3333 | 0.5000 | 0.3333 | 0.3066 | 1.0000 |
| Sources of food | 0.3333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Strengths and weaknesses of dense retrieval | 0.5000 | 0.5000 | 0.4722 | 0.4032 | 1.0000 |
| The importance of chunking | 0.3333 | 0.5000 | 0.5000 | 0.3832 | 1.0000 |
| Training dense retrieval models | 0.2667 | 0.8000 | 0.7000 | 0.7262 | 0.8000 |
| When food is consumed | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| Why cosine similarity is preferred | 0.3333 | 1.0000 | 0.6667 | 0.7540 | 1.0000 |

---

# 6. Major Findings

## 6.1 Retrieval has a strong recall/hit-rate foundation

The system achieves:

**Recall@3: 0.6029**

and:

**Hit Rate@3: 0.8479**

This indicates that the system is frequently capable of finding relevant information within the top three results.

This is an important baseline strength.

The system is therefore not failing universally at semantic retrieval.

---

## 6.2 Ranking precision is the primary weakness

Precision@3 is only:

**0.3226**

This means that the top-three result set often contains chunks that are not the expected relevant chunks.

The system appears to understand broad semantic relationships, but has difficulty distinguishing between closely related pieces of information.

For example, several failed queries retrieve chunks from the correct document but the wrong section.

This is particularly visible in the food, IR, dense retrieval, and RAG portions of the corpus.

---

## 6.3 Some failures are systematic rather than query-specific

Several groups of semantically similar queries produce the exact same incorrect ranking.

For example:

### Creators of food

Both:

> Where did food come from?

and:

> What are the sources of food?

retrieve:

```text
011-003
011-001
011-004