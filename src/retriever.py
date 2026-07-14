from similarity import cosine_similarity


class Retriever:
    # Constructor 
    # Remember the document collection 
        def __init__( 
            self,
            documents
        ):
        self.documents = documents # store the documents that were passed in as part of this retriever object
    
    # Search
    # 1. Create empty results
    # 2. Commpare query embedding to every document
    # 3. Store document + score
    # 4. Sort descending
    # 5. Return top_k

def search(self, query_embedding, top_k=3):
        results = []
        for doc in self.documents:
            score = cosine_similarity(query_embedding, doc.embedding)

            results.append(doc, score))

 # 4. Sort descending
        results.sort(key=lambda x: x['score'], reverse=True)
        
        # 5. Return top_k
        return results[:top_k]
            
    



