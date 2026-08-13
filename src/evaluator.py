from evaluation import (
    precision_at_k,
    recall_at_k,
    mean_reciprocal_rank,   
    dcg_at_k,
    ndcg_at_k,
    hit_rate_at_k,
)

#====================================================================
# Run every benchmark query through the retrieval system and
# compare the results aaginst labeled ground truth
#====================================================================

def evaluate(retrieval_system, benchmark, k):

