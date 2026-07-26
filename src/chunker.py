"""
# chunker.py

# Splits documents into sentence-based chunks for granular retrieval.
# Each sentence becomes a separate retrievable unit.
"""


from document import Document
from chunk import Chunk


class Chunker:
    """
    Converts a Document into a list of sentence-based Chunk objects.

    This class is stateless. Eaach document is processed independently.

    """

    def __init__(self):
        pass 

    def chunk(self, document: Document):

        chunks = [] 

        # Read the document text.
        text = document.text

        # Slit into sentences.
        sentences = text.split(".")

        # Create one Chunk per sentence. 
        for chunk_number, sentence in enumerate(sentences, start=1):

            # Remove leading/trailing whitespace.
            sentence = sentence.strip()

            # Skip empty sentences
            if not sentence:
                continue
            
            chunk = Chunk(
                    id = f"{document.id}-{chunk_number:03d}",
                    document_id = document.id,
                    text = sentence,
                )

            chunks.append(chunk)
       
        return chunks



# ========================================
# Generate chunk embeddings
#=========================================

chunker = Chunker()
all_chunks = []
chunker.chunk(document.text)