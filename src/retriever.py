"""
retriever.py

Retrieves the most relevant documents from a corpus using
semantic similarity between query and document embeddings.

The Retriever does not generate embeddings or load documents.
It only compares vectors and ranks results.
"""

from document import Document
from similarity import cosine_similarity



class Retriever:
    """
    Performs semantic retrieval over a collection of documents.
    """

    def __init__(self, documents: list[Document]):
        """
        Store the document collection.

        Parameters
        ----------
        document : list[Document]
            Documents that have already been embedded.
        """
        self.documents = documents 
    

    def search(
        self, 
        query_embedding: list[float], 
        top_k: int = 3
    ) -> list[tuple[Document, float]]:
        
        """
        Retrieve the most similar documents to a query.

        Parameters
        ----------
        query_embedding : list[float]
            Vector representation of the user's query.

        top_k : int
            Number of results to return.

        Returns
        -------
        list[tuple[Document, float]]
            Documents paired with their similarity scores,
            sorted from highest similarity to lowest.
        """

        results = []

        # Compare the query against every document
        for document in self.documents:

            score = cosine_similarity(
                query_embedding, 
                document.embedding
            )

            results.append(
                (document, score)
            )

        # Rank documents by similarity score
        results.sort(
            key=lambda item: item[1], 
            reverse=True
        )
        
        # Return only the best matches
        return results[:top_k]
            
    



