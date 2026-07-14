"""
similarity.py
Utility functions for comparing vector embeddings.

Currently this module implements cosine similarity, which measures
how semantically similar two embedding vectors are.

This module is intentionally independent of the reat of the retrieval 
pipeline. It operates only on vectors
"""

import math



def cosine_similarity(
    vector_a: list[float], 
    vector_b: list[float]
) -> float:
    """
    Compute the cosine similarity between two vectors.

    Parameters
    ----------
    vector_a : list[float]
        First embedding vector.
    
    vector_b : list[float]
        Second embedding vector
    
    Returns
    -------
    float
        Cosine similarity between the vectors. 

        +1.0 = identical direction
         0.0 = unrelated
        -1.0 = opposite direction
    """

    # Check to make sure vectors are same length
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions.") 
    
    # Compute the dot product
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))

    # Compute each vector's magnitude
    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))
    
    # Prevent division by zero
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    
    # Cosine similarity formula
    return dot_product / (magnitude_a * magnitude_b)


