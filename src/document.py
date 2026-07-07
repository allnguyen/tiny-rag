from dataclasses import dataclass
from typing import Optional

@dataclass
class Document:
    id: str
    title: str
    filename: str
    text: str
    filepath: str

    #from typing import Optional

    #embedding: Optional[list[float]] = None