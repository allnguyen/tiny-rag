from config import DOCUMENTS_PATH
from loader import loader_function 





documents = loader_function(DOCUMENTS_PATH) # calls loader_function with directory path and stores variable called documents. returns list for later
#generator = EmbeddingGenerator()


print(f"\n Documents loaded: {len(documents)}") # prints the number of documents that were loaded.

if documents: # checks if the documents list has any items or successfully loaded
    print("\n Documents Titles:")
    for doc in documents:
        print(f"    {doc.id}: {doc.title}")
else:
    print("No documents found.")
                                    

#for document in documents:
    #document.embedding = generator.generate(document.text)