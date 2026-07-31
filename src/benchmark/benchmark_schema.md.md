# TinyRAG Benchmark Schema

This document describes the JSON schema used by TinyRAG Benchmark.

---

# Benchmark Structure

The benchmark is stored as a JSON array.

Each object represents a single **information need**.

```json
[
  {
    ...
  },
  {
    ...
  }
]
```

---

# Schema

```json
{
  "id": 1,

  "information_need": "Definition of Information Retrieval",

  "description": "The user wants to understand what Information Retrieval is.",

  "queries": [
    "What is Information Retrieval?",
    "Define Information Retrieval.",
    "Explain IR."
  ],

  "relevant_chunks": [
    "001-001"
  ]
}
```

---

# Field Definitions

## id

Unique integer identifier.

Rules:

* Must be unique.
* Never reused.
* Remains stable across benchmark revisions.

Example

```json
"id": 17
```

---

## information_need

A concise description of the underlying concept being tested.

This field represents **what the user wants to know**, not the wording of a particular query.

Example

```json
"information_need": "Definition of Dense Retrieval"
```

---

## description

A human-readable explanation of the information need.

This field is intended for documentation only and is not used by the evaluation pipeline.

Example

```json
"description": "The user wants to understand what Dense Retrieval is and how it differs from lexical retrieval."
```

---

## queries

A list of realistic user queries that express the same information need.

Guidelines:

* Include multiple natural phrasings.
* Include abbreviations when appropriate.
* Include beginner and technical wording.
* Avoid duplicate paraphrases.
* Keep all queries focused on the same information need.

Example

```json
"queries": [
  "What is BM25?",
  "Explain BM25.",
  "Define BM25.",
  "How does BM25 work?"
]
```

---

## relevant_chunks

The manually curated ground-truth chunk IDs.

Rules:

* Must reference valid chunk IDs.
* Multiple chunk IDs are allowed.
* Order does not matter.
* Labels are assigned manually after reviewing the chunked corpus.

Example

```json
"relevant_chunks": [
  "004-002",
  "004-003"
]
```

---

# Labeling Guidelines

A chunk should be labeled as relevant if it substantially answers the information need.

Multiple chunks may be relevant when:

* both independently answer the question,
* they provide complementary evidence,
* they contain overlapping explanations.

A chunk should **not** be labeled simply because it mentions the topic.

---

# Evaluation Workflow

For each benchmark entry:

1. Execute every query in the `queries` list.
2. Retrieve the Top-K chunk IDs.
3. Compare retrieved chunk IDs with `relevant_chunks`.
4. Compute retrieval metrics.
5. Aggregate metrics across the entire benchmark.

---

# Versioning

Benchmark releases should be versioned.

Example:

```
benchmark/
    benchmark_v1.json
    benchmark_v2.json
    README.md
    benchmark_schema.md
```

Existing IDs should remain stable whenever possible to preserve comparability across benchmark versions.

---

# Design Principles

TinyRAG Benchmark follows several guiding principles:

* Evaluate information needs rather than individual questions.
* Separate language generation from relevance labeling.
* Support multiple query formulations.
* Support multiple relevant chunks.
* Keep the benchmark reproducible and human-readable.
* Use standard Information Retrieval evaluation metrics.
