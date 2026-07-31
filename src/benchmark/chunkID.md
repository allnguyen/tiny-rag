Total chunks created: 61

001-001: Information Retrieval (IR) is the field of designing systems that find relevant information from a large collection of documents in response to a user query
001-002: The goal is not just to store data, but to rank and retrieve the most relevant content efficiently
001-003: IR systems typically operate over a corpus of documents and take a user query as input
001-004: The system outputs a ranked list of documents based on estimated relevance
001-005: Traditional IR methods rely on lexical matching (matching words), while modern systems often combine lexical and semantic methods,
001-006: Core components of IR systems include document indexing, query processing, ranking functions, and evaluation metrics such as precision, recall, and nDCG
001-007: IR is foundational to search engines, recommendation systems, and modern retrieval-augmented generation (RAG) systems
002-001: Embeddings are dense vector representations of text where semantic meaning is encoded in a continuous numerical space
002-002: Each piece of text is mapped to a high-dimensional vector, typically produced by neural networks
002-003: The key idea is that semantically similar texts are close together in vector space, measured using similarity metrics such as cosine similarity
002-004: For example, “car” and “automobile” would have similar embeddings even if they share no exact words
002-005: Embedding models are trained on large corpora using objectives that encourage semantic similarity to be reflected geometrically
002-006: Embeddings are used in search, clustering, classification, and retrieval systems
002-007: In RAG systems, embeddings allow queries and documents to be compared based on meaning rather than exact keyword overlap
003-001: Cosine similarity is a metric used to measure the similarity between two vectors by computing the cosine of the angle between them
003-002: It is widely used in embedding-based retrieval systems
003-003: The formula compares the dot product of two vectors divided by the product of their magnitudes
003-004: Cosine similarity ranges from -1 to 1, where 1 means the vectors are identical in direction, 0 means orthogonal (unrelated), and -1 means opposite
003-005: In text retrieval, cosine similarity is preferred because it focuses on direction rather than magnitude, making it robust for comparing embedding vectors
003-006: It is a core operation in nearest neighbor search when retrieving relevant documents from an embedding database
004-001: BM25 is a ranking function used in traditional search engines for lexical retrieval
004-002: It is based on probabilistic information retrieval and improves upon TF-IDF
004-003: BM25 scores documents based on term frequency (how often query terms appear), inverse document frequency (how rare the terms are across the corpus), and document length normalization
004-004: A key feature of BM25 is diminishing returns: repeated occurrences of a term increase relevance, but with decreasing impact
004-005: BM25 works well when exact keyword matches are important but does not capture semantic meaning or paraphrasing
004-006: It remains widely used in hybrid search systems because of its speed, interpretability, and strong performance on keyword-heavy queries
005-001: Dense retrieval is a method of searching documents using embedding similarity instead of keyword matching
005-002: Both queries and documents are converted into dense vector embeddings
005-003: Retrieval is performed by finding the nearest neighbors to the query vector in embedding space using similarity metrics like cosine similarity
005-004: Unlike BM25, dense retrieval can match semantically similar content even when no exact words overlap
005-005: Dense retrieval is typically implemented using neural embedding models trained on large datasets
005-006: It is more effective than lexical methods for paraphrased queries but can struggle with exact keyword specificity unless combined with other methods
006-001: Vector databases are specialized systems designed to store and search high-dimensional embedding vectors efficiently
006-002: They support approximate nearest neighbor (ANN) search, allowing fast retrieval of similar vectors even in large datasets
006-003: Examples include FAISS, Chroma, Pinecone, and Weaviate
006-004: Vector databases typically store embeddings alongside metadata such as document IDs and source text
006-005: They optimize search using indexing techniques like HNSW or IVF
006-006: They are a core infrastructure component in modern RAG systems because they enable scalable semantic search
007-001: Chunking is the process of splitting long documents into smaller segments before generating embeddings
007-002: This is necessary because embedding models have token limits and because smaller units improve retrieval precision
007-003: Common chunking strategies include fixed-size token splitting, sentence-based splitting, and structure-aware splitting using headings or markdown
007-004: Chunk size affects retrieval quality: small chunks improve precision but may lose context, while large chunks preserve context but reduce specificity
007-005: Overlapping chunks are often used to prevent important information from being split across boundaries
007-006: Chunking is a critical design decision in RAG systems and strongly influences downstream retrieval performance
008-001: Reranking is a second-stage retrieval process that refines an initial set of retrieved documents
008-002: After a fast retrieval step (BM25 or dense search), a more accurate but slower model is used to reorder results
008-003: Rerankers often use cross-encoders that jointly encode query-document pairs to compute relevance scores
008-004: This improves retrieval quality by capturing finer-grained semantic relationships than initial embedding-based search
008-005: Reranking is commonly used in production systems to balance speed and accuracy
008-006: It is especially useful when the first-stage retriever returns a large candidate set with mixed relevance
009-001: Hybrid search combines lexical retrieval methods like BM25 with dense retrieval methods based on embeddings
009-002: The goal is to leverage the strengths of both approaches
009-003: BM25 is strong at exact keyword matching, while dense retrieval is strong at semantic similarity
009-004: Hybrid systems typically combine scores from both methods using weighted sums or merge ranked lists
009-005: This approach improves robustness across different query types, including both keyword-heavy and paraphrased queries
009-006: Hybrid search is widely used in production RAG systems because it provides better coverage and reduces failure cases of single-method retrieval
010-001: Retrieval-Augmented Generation (RAG) is a framework that enhances large language models by retrieving relevant documents before generating a response
010-002: The pipeline consists of indexing a document corpus, retrieving relevant documents based on a query, and passing those documents as context into a language model
010-003: RAG reduces hallucination by grounding model outputs in external knowledge
010-004: The quality of a RAG system depends heavily on retrieval quality, including embedding models, chunking strategy, and ranking methods
010-005: RAG systems are widely used in question answering, enterprise search, and knowledge assistants