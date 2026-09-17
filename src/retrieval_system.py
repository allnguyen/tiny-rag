"""
retrieval_system.py

Coordinates dense retrieval and cross-encoder reranking.
"""

from retriever import Retriever
from reranker import CrossEncoderReranker
from config import RETRIEVAL_TOP_K, RERANKER_CANDIDATE_K
from chunk import Chunk


class RetrievalSystem:

    def __init__(
        self,
        retriever: Retriever,
        reranker: CrossEncoderReranker,
    ):

        self.retriever = retriever
        self.reranker = reranker


    def search(
        self,
        query: str,
        top_k: int = RETRIEVAL_TOP_K,
        candidate_k: int = RERANKER_CANDIDATE_K,
    ) -> list[tuple[Chunk, float]]:

        # Stage 1:
        # Retrieve a larger set of candidates using dense retrieval.
        candidates = self.retriever.search(
            query,
            top_k=candidate_k,
        )

        # Stage 2:
        # Rerank candidates using the cross-encoder.
        results = self.reranker.rerank(
            query=query,
            candidates=candidates,
            top_k=top_k,
        )

        return results

    def search_with_diagnostics(
            self,
            query: str,
            top_k: int = 3,
            candidate_k: int = RERANKER_CANDIDATE_K,
        ):
    
            candidates = self.retriever.search(
                query,
                top_k=candidate_k,
            )
    
            results = self.reranker.rerank(
                query=query,
                candidates=candidates,
                top_k=top_k,
            )
    
            return candidates, results