"""
config.py

Central location for project configuration.

Keeping configuration separate from implementation makes it easier
to change models, paths, or system settings without modifying core code.
"""

# Location of the text document corpus
DOCUMENTS_PATH = (
    r"C:\Users\allan\Projects\experiments\tiny-rag\documents"
)

# Ollama configuration
OLLAMA_URL = "http://localhost:11434/api/embed"

# Embedding model used to convert text into vectors
EMBEDDING_MODEL = "nomic-embed-text"

# Optional metadata.
# None means we allow the modelto determine the dimension.
# Example: nomic-embed-text produces 769 dimensions
EMBEDDING_DIMENSIONS = None