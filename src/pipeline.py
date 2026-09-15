from config import DOCUMENTS_PATH

from loader import loader_function
from chunker import Chunker
from embedding import EmbeddingGenerator

from retriever import Retriever
from reranker import CrossEncoderReranker
from retrieval_system import RetrievalSystem

def build_retrieval_system():

    # ====================================================================================
    # 1. Load documents
    documents = loader_function(
        DOCUMENTS_PATH
    )
    # ====================================================================================

    if not documents:
        raise ValueError(
            "No documents found."
        )
    # =====================================================================================
    # 2. Chunk documents
    # =====================================================================================

    chunker = Chunker()

    all_chunks = []

    for document in documents:

        chunks = chunker.chunk(
            document
        )

        all_chunks.extend(
            chunks
        )
    # ==========================================================================================
    # 3. Generate embeddings
    # ==========================================================================================

    embedding_generator = (
        EmbeddingGenerator()
    )

    for chunk in all_chunks:

        chunk.embedding = (
            embedding_generator.generate(
                chunk.text
            )
        )
    # ======================================================================================
    # 4. Initialize retriever
    # ======================================================================================

    retriever = Retriever(
        all_chunks,
        embedding_generator,
    )

    # ======================================================================================
    # 5. Initialize cross-encoder reranker
    # ======================================================================================
    reranker = CrossEncoderReranker()

    # =======================================================================================
    # 6. Build complete retrieval system
    # =======================================================================================

    retrieval_system = RetrievalSystem(
        retriever=retriever,
        reranker=reranker,
    )
    return retrieval_system