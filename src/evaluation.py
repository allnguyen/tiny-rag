import numpy as np

def precision_at_k(actual, predicted, k):
    """
    Porportion of recommended items in the top-K that are relevant.
    """
    if k <= 0:
        return 0.0
    top_k_pred = predicted[:k]
    relevant_retrieved = len(set(top_k_pred) & set(actual))
    return relevant_retrieved / k

def recall_at_k(actual, predicted, k):
    """
    Proportion of all relevant items that are captured in the top-K.
    """
    if k <= 0:
            return 0.0
    if not actual:
        return 0.0
    top_k_pred = predicted[:k]
    relevant_retrieved = len(set(top_k_pred) & set(actual))
    return relevant_retrieved / len(actual)

def mean_reciprocal_rank(actual, predicted):
    """
    Finds the rank of the *first* relevant item and returns 1/rank.
    """
    for index, item in enumerate(predicted):
        if item in actual:
            return 1 / (index + 1) 
    return 0.0

def dcg_at_k(actual, predicted, k):
    """
    Discounted Cumulative Gain using binary relevance (1 if in actual, 0 if not).
    """
    top_k_pred = predicted[:k]
    score = 0.0
    for index, item in enumerate(top_k_pred):
        if item in actual:
            # Using the standard log2 formulation for rank discount
            score += 1.0 / np.log2(index + 2)
    return score

def ndcg_at_k(actual, predicted, k):
    """
    Normalized Discounted Cumulative Gain.
    """
    dcg = dcg_at_k(actual, predicted, k)

    # Ideal DCG trats the actual relevant items as if they were perfectly ranked first
    ideal_actual = list(actual)[:k]
    idcg = dcg_at_k(actual, ideal_actual, k)

    if idcg == 0:
        return 0.0
    return dcg / idcg