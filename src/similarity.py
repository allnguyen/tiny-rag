import math

def cosine_similarity(vector_a, vector_b):

    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same dimensions.") # Check to make sure vectors are same length
    
    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    magnitude_a = math.sqrt(sum(a * a for a in vector_a))
    magnitude_b = math.sqrt(sum(b * b for b in vector_b))
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    
    return dot_product / (magnitude_a * magnitude_b)


"""

-1.0 <= cosine_similarity <= 1.0
        cosine-similarity  = 0 ---> Vectors are orthogonal, no directional correlation or similarity
        cosine_similarity  = -1.0 ----> vectors are diametrically opposed and point in completely opposite directions
        cosine_similarity  = 1.00 ----> Vectors are identical and point in the exact same direction
0.80 <= cosine_similarity <= 0.99 ----> Highly similar
0.20 <= cosine_similarity <= 0.50 ----> Moderately/tangentially related
0.00 <= cosine_similarity <= 0.10 ----> Generally unrelated
"""

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
score = cosine_similarity(vector_a, vector_b)
print(f"Cosine similarity: {score:.4f}")