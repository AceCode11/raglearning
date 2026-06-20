from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from bs4 import BeautifulSoup


URL = "https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/"


def extract_text(html: str) -> str:
    """
    Clean HTML content and return plain text.
    """

    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    return soup.get_text(separator=" ", strip=True)


def load_and_chunk():
    """
    Load Azure Bicep documentation and split into chunks.
    """

    loader = RecursiveUrlLoader(
        url=URL,
        max_depth=2,
        extractor=extract_text
    )

    docs = loader.load()

    print(f"Loaded {len(docs)} documents")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    print(f"Created {len(chunks)} chunks")

    return chunks


if __name__ == "__main__":

    chunks = load_and_chunk()

    print("\nSample Chunk:\n")
    print(chunks[0].page_content[:500])

    print("\nMetadata:\n")
    print(chunks[0].metadata)