import os 
from document import Document


# Simple loader that reads all txt files from a directory 

def loader_function(directory_path):
    documents: list[Document] = [] 
    files = sorted([f for f in os.listdir(directory_path) if f.endswith(".txt")])
    
    if not files:
        print(f"No .txt files found in '{directory_path}'")
        return documents
    
    for idx, filename in enumerate(files, 1):
        filepath = os.path.join(directory_path, filename)
       
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()

        doc = Document(
            id=f"{idx:03d}",
            title=filename[4:-4].replace('_',' '),
            filename=filename, 
            text=text, 
            filepath=filepath
        )
        
        documents.append(doc) 
    return documents



