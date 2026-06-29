from loader import loader_function # import loader_function from file loader.py in the same directory

directory_path = r"C:\Users\allan\Projects\experiments\tiny-rag\documents" # Creates variable that stores path to documents folder

documents = loader_function(directory_path) # calls loader_function with directory path and stores variable called documents. returns list for later

print(f"\n Documents loaded: {len(documents)}") # prints the number of documents that were loaded.

if documents: # checks if the documents list has any items or successfully loaded
    print("\n Documents Titles:")
    for doc in documents:
        print(f"    {doc['id']}: {doc['title']}")
else:
    print("No documents found.")
                                    