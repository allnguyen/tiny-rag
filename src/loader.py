"""
loader.py

Loads all text documents from the corpus directory and converts them 
into Document objects.

The loader is responsible only for reading files from disk and creating 
Document instances. It does not generate embeddings or perform retrieval.
"""




import os 

from document import Document




def loader_function(directory_path: str) -> list[Document]:
    """
    Load every .txt file from a directory.

    Parameters
    ----------
    directory_path : str
        Path to the document corpus. 
    
    Returns
    -------
    list[Document]
        A list of Document objects
    """
    
    documents: list[Document] = []

    # Read every text file in alphabetical order
    files = sorted(
        file 
        for file in os.listdir(directory_path) 
        if file.endswith(".txt")
    )
    
    if not files:
        print(f"No .txt files found in '{directory_path}'")
        return documents
    
    # Create one Document object for each file
    for index, filename in enumerate(files, 1):

        filepath = os.path.join(directory_path, filename)
       
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()

        document = Document(
            id=f"{index:03d}",
            title=filename[4:-4].replace("_"," "),
            filename=filename, 
            text=text, 
            filepath=filepath,
        )
        
        documents.append(document)

    return documents



