"""
chunk.py

Represents the smallest retrievable unit of information.

A Chunk belongs to a parent Document and is the primary unit
used during semantic retrieval.

"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class Chunk:
    """
    Represents a single chunk
    """
    id: str
    document_id: str
    text: str 
    embedding: Optional[list[float]] = None 




