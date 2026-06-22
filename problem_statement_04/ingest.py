from langchain_core.documents import Document

from clone_repo import clone_repository
from scanner import scan_repository
import os 


supported_extensions = {
    ".py" , ".js" , ".jsx" , ".cpp" , ".c" , 
    ".md" , ".txt" , ".yml" , ".yaml" , ".json" , ".html"
}

def load_repository(repo_url):
    repo_path = clone_repository(repo_url)


    files = scan_repository(repo_path)

    documents = []

    for file in files:
        extension = os.path.splitext(file)[1]
        
        
        if extension not in supported_extensions:
            continue
        
        
        try: 
            with open(file , "r" , encoding = "utf-8") as f:


                content = f.read()

            document = Document(
                page_content = content , 
                metadata = {
                    "file_name": os.path.basename(file) , 
                    "file_type" : extension , 
                    "file_path" : file
                }
            )

            documents.append(document)

        except Exception as e:
            print(f"error reading {file} : {e}")

    return documents



