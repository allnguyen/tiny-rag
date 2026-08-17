"""
retriever.py


Performs semantic retrieval over a collection of embedded chunks.

Given a text query, the Retriever generates a query embedding,
computes cosine similarity between the query and every chunk
embedding, ranks the results, and returns the top-k most relevant
chunks.

The Retriever is responsible only for retrieval and query
embedding generation. It does not:
- load files
- generate chunk embeddings
- communicate with an LLM
- perform prompt engineering
"""

from chunk import Chunk
from similarity import cosine_similarity
from embedding import EmbeddingGenerator



class Retriever:
    """
    Retrieves the most semantically similar chunks from an embedded corpus.
    """

    def __init__(
        self, 
        chunks: list[Chunk],
        embedding_generator: EmbeddingGenerator,
    ):
        self.chunks = chunks 
        self.embedding_generator = embedding_generator
    

    def search(
        self, 
        query: str,
        top_k: int = 3
    ) -> list[tuple[Chunk, float]]:
        
        """
        Retrieve the top-k chunks most similar to a text query.

        Args:
            query: User's text query
            top_k: Maximum number of results to return.

        Returns:
            A list of (Chunk, similarity_score) tuples sorted 
            in descending order of cosine similarity.
        """
        # Converts query text into an embedding
        query_embedding = self.embedding_generator.generate(query)

        results: list[tuple[Chunk, float]] = []

        # Compare the query against every chunk 
        for chunk in self.chunks:

            score = cosine_similarity(
                query_embedding, 
                chunk.embedding,
            )

            results.append(
                (chunk, score)
            )
            

        # Rank by similarity 
        results.sort(
            key=lambda item: item[1], 
            reverse=True
        )
        
        
        return results[:top_k]
            
    



