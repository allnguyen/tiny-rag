Tiny RAG (Retrieval-Augmented Generation)
A small learning project to better understand how Retrieval-Augmented Generation (RAG) systems work. 

Overview:
This project explores the core components of a RAG pipeline by combining document retrieval with a Large Language Model (LLM) to answer questions using external knowledge.

The goal is to gain hands-on experience with modern AI application development rather than build a production-ready system. 

Features:
- Load and process text documents
- Split documents into smaller chinks
- Generate embeddings for document chunks
- Store and retrieve relevant information from a vector database
- Retrieve the most relevant context for user's question
- Send retrieved context to an LLM to generate grounded responses

Technologies: 
- Python
- LLM APIs
- Embeddings
- Vector database
- Retrieval-Augmented Generation (RAG)

Learning Goals
This project helped me understand:
- The architecture of RAG systems
- Document chunking strategies
- Semantic search using embeddings
- Context retrieval
- Prompt construction for grounded responses
- End-to-end LLM application development

Why I Built This
I'm interested in AI infrastructure and machine learning applications. As someone with experience in AI data annotation and evaluation, I wanted to better understand how retreival systems work behind modern LLM-powered applications. 

Current Status:

High-Level Architecture

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
Document.embedding               cosine_similarity()
        │                                 │
        └──────────────┬──────────────────┘
                       ▼
             Similarity Scores
                       ▼
              Sort Highest → Lowest
                       ▼
                Return Top-k Results


Everything begins with a corpus of text documents. 
-----------------------------------------------------------------------------------------------------------
Component Overview:

1. Document

Responsibility: Represent a single document within a corpus. 
A Document contains metadata together with its text and eventually its embedding vector. 

Document
├── id
├── title
├── filename
├── filepath
├── text
└── embedding

Under Single Responsibility Principle, a Document does not know how to:
- generate embeddings
- retrieve itself
- rank itself
- compute similarity

It simply stores information. 

2. Loader

Responsibility: Read every text file from disk and create Document objects. 

Input:
documents/

Output:
list[Document]

The loader is the only component that understands:
- folders
- filenames
- file I/O
- UTF-8 encoding

Every other component receives already-loaded Document objects.

3. EmbeddingGenerator

Responsibility: Convert natural language into numerical vector representations.

Input: 
text

Output: 
list[float]

Internally it communicates with Ollama. 
Under principle of encapsulation, the other components never needs to know
- API endpoints
- embedding model names
- HTTP requests
Those details are hidden inside the class.

4. Cosine similarity

Responsibility: Measure semantic similarity between two vectors. 

Input:
vector A
vector B

Output: 
float

The function only performs mathematics, has no permanent state, therefore, is implemented as a 
standalone function rather than a class. 

Under Single Responsibility Principle, it knows nothing about
- documents
- retrieval
- AI

5. Retriever

Responsibility: Find the most relevant documents

Input: 
query embedding

Output:
list[(Document, score)]

Internally it:
- iterates through every document
- compares embeddings
- computes cosine similarity
- stores results
- sorts results
- returns the top k

Retriever does not kow how embeddings were created, it assuems document already contains one. 

6. Main

Responsibility: Coordinate the entire pipeline.

Main contains almost no business logic, orchestrates components in sequence, and effectively the conductor of the application. 
--------------------------------------------------------------------------------------------------------
Current Limitations:

1. Whole-document retrieval 
Current 1 embedding = 1 document. Eventually, we will transition this project to retrieve chunks
to emulate more a production RAG system. 

2. No vector index
Every search compares every document. There is no acceleration.

3. Embeddings regenerated every execuation. Every run recomputes embeddings.
Eventually, we will transition this project to precompute and persist embeddings. 

4. No evaluation
This system currently has measurements under development such as:
- Recall@k
- MRR
- Precision
- Latency

5. No reranking 
Ranking currently is determined solely by similarity score. Eventually we will develop second-stage reranker. 

6. No Language model
We will develop generation. 