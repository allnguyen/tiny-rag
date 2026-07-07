import ollama

from config import EMBEDDING_MODEL, OLLAMA_URL


class EmbeddingGenerator:
        def __init__(
            self, 
            embedding_model=EMBEDDING_MODEL, 
            ollama_url=OLLAMA_URL
        ):
            self.model = embedding_model
            self.ollama_url=ollama_url

        def generate(self, text: str) -> list[float]:
            response = ollama.embed(            # Call Ollama
                model = self.model,
                input = text,
            )

            vector = response["embeddings"][0]   
            
            return vector







