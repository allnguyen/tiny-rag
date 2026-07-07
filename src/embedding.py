from dataclasses import dataclass
import ollama
import chromadb
from loader import loader_function
# Create an EmbeddingGenerator class

class EmbeddingGenerator:
    def _init_(self, OLLAMA, EMBEDDING_MODEL):
        self.OLLAMA = "http://localhost:11434/api/embed" 
        self.EMBEDDING_MODEL = "nomic-embed-text"

# Get text
from loader import loader_function(directory_path)

#Accept a string and generate text to list method
def generate_embeddings(text: List[str]) -> List[float]:
        """ Accepts a list of strings and returns a list of float vectors. """

# 2. CALL OLLAMA 
    _init_(
    LLAMA = "http://localhost:11434/api/embed"
    EMBEDDING_MODEL = "nomic-embed-text"

)

# Generate embeddings

ollama pull nomic-embed-text
client = chromadb.Client()
collection = client.create_collection(name="docs")

#store each document in a vector embedding database
for i,d in enumerate(documents):
    response = ollama.embed(model="nomic-embed-text", input=d)
    embeddings = response["emmbeddings"]
    collection.add(
        ids=[str(i)],
        embeddings = embeddings,
        documents=[d]
    )


print(output['response'])

"""



"""
3. Return the embedding
    print(Embedding)

4. Raise an error if something goes wrong