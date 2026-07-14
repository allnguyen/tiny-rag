"""
document.py

Defines the Document data model used throughout the retrieval pipeline. 

A Document represents one source document in the corpus. 
It stores the document's metadata, raw text, and (later) its vector embedding. 

This class intentionally contains no retrieval or embedding logic.
Its responsibility is simply to hold data

"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Document:
    """
    Represents a single document in the corpus.
    """

    # Unique identifier assigned by loader
    id: str
    
    # Human-readable document title
    title: str

    # Original filename
    filename: str

    # Full document contents
    text: str

    # Location of the document on disk
    filepath: str
    
    # Vector representation of the document
    # None until embeddings are generated
    embedding: Optional[list[float]] = None





