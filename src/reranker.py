"""
reranker.py

Cross-encoder reranker for TinyRAG.

Receives candidate chunks from the dense retriever,
scores each query-chunk pair, and returns the
most relevant chunks in reranked order.
"""

from chunk import Chunk
from sentence_transformers import CrossEncoder
from config import RERANKER_MODEL


class CrossEncoderReranker:

    def __init__(
        self,
        model_name: str = RERANKER_MODEL,
    ):
        print("Loading cross-encover reranker...")
        # Load reranker model 
        self.model = CrossEncoder(model_name)
        print("Cross-eocoder reranker loaded.")
        


    def rerank(
        self,
        query: str,
        candidates: list[tuple[Chunk, float]],
        top_k: int = 3,
    ) -> list[tuple[Chunk, float]]:

        # Create query-chunk pairs for the cross-encoder.
        pairs = [
            (query, chunk.text)
            for chunk, _ in candidates
        ]

        # Score every query-chunk pair.
        scores = self.model.predict(pairs)

        # Combine chunks with their new cross-encoder scores.
        reranked_results = [
            (chunk, float(score))
            for (chunk, _), score in zip(
                candidates, 
                scores
            )
        ]

        # Sort highest relevance score first.
        reranked_results.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        # Return only the final top-K results.
        return reranked_results[:top_k]