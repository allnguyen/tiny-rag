"""
retriever.py

Performs semantic retrieval over a collection of embedded chunks.

Given a query embedding, the Retriever computes the cosine similarity
between the query and every chunk embedding, ranks the results, and
returns the top-k most relevant chunks.

The Retriever is responsible only for retrieval. It does not:
- load files
- generate embeddings
- communicate with an LLM
- perform prompt engineering
"""

from chunk import Chunk
from similarity import cosine_similarity



class Retriever:
    """
    Retrieves the most semantically similar chunks from an embedded corpus.
    """

    def __init__(self, chunks: list[Chunk]):
        """
        Initialize the Retriever.

        Args:
            chunks: A collection of Chunk objects with precomputed embeddings.
        """
        self.chunks = chunks 
    

    def search(
        self, 
        query_embedding: list[float], 
        top_k: int = 3
    ) -> list[tuple[Chunk, float]]:
        
        """
        Retrieve the top-k chunks most similar to a query.

        Args:
            query_embedding: Embedding vector representing the user's query.
            top_k: Maximum number of results to return.

        Returns:
            A list of (Chunk, similarity_score) tuples sorted in
            descending order of cosine similarity.
        """
        results: list[tuple[Chunk, float]] = []

        # Compare the query against every chunk in the corpus
        for chunk in self.chunks:

            score = cosine_similarity(
                query_embedding, 
                chunk.embedding,
            )

            results.append((chunk, score))
            

        # Rank chunks by similarity score
        results.sort(
            key=lambda item: item[1], 
            reverse=True
        )
        
        # Return only the best matches
        return results[:top_k]
            
    



