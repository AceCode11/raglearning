import ast
from langchain_core.documents import Document

def chunk_documents(documents):
    chunks = []

    for doc in documents:

        file_name = doc.metadata["file_name"]

        if not file_name.endswith(".py"):
            continue

        try:
            tree = ast.parse(doc.page_content)

            for node in ast.walk(tree):
                if isinstance(
                    node , 
                    ast.FunctionDef

                ):
                    

                    function_name = node.name
                    function_code =ast.get_source_segment(
                        doc.page_content , 
                        node
                    )



                    chunk = Document(
                        page_content = function_code , 

                        metadata = {
                            **doc.metadata , 
                            "function_name" : function_name
                        }
                    )

                    chunks.append(chunk)

                    
        except Exception as e:
            print(
                f"Error in {file_name} : {e}"
            )
    return chunks


if __name__ == "__main__":

    from ingest import load_repository

    repo_url = input(
        "GitHub URL: "
    )

    docs = load_repository(
        repo_url
    )

    chunks = chunk_documents(
        docs
    )

    print(
        f"Total Chunks: {len(chunks)}"
    )

    print("\n")

    print(
        chunks[0].metadata
    )

    print("\n")

    print(
        chunks[0].page_content[:500]
    )