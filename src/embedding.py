import ollama

class EmbeddingGenerator:
        def __init__(self, embedding_model='EMBEDDING_MODEL')
            self.model = embedding_model

def embedding_generator(self, text):
    response = ollama.embed(            # Call on Ollama
        model = self.model
        input = text
    )
    vector = response['embeddings'][0]   
    return vector

# Initialize generator
generator = EmbeddingGenerator(embedding_model='EMBEDDING_MODEL')




# In official Ollama Python library, the ollama.embed response dictionary 
# returns a list under the key 'embeddings'


