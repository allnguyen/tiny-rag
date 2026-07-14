"""
embedding.py

Generates vector embeddings using a local Ollama embedding model.

The EmbeddingGenerator is responsible only for converting natural
language text into numerical vector representations.

It does not know where text comes from or how embeddings will be used.
"""


import ollama

from config import EMBEDDING_MODEL
from config import OLLAMA_URL


class EmbeddingGenerator:
        """
        Generate embeddings using a local Ollama model.
        """

        def __init__(
            self, 
            embedding_model: str = EMBEDDING_MODEL, 
            ollama_url: str = OLLAMA_URL,
        ):
            """
            Store configuration for future embedding requests.
            """

            self.model = embedding_model
            self.ollama_url = ollama_url

        def generate(self, text: str) -> list[float]:
            """
            Generate an embedding vector for a piece of text.

            Parameters
            ----------
            text : str
                Input text.
            
            Returns
            -------
            list[float]
                Embedding vector.
            """

            response = ollama.embed(            
                model = self.model,
                input = text,
            )

            vector = response["embeddings"][0]   
            
            return vector







