from ingest import load_repository


repo_url = input(
    "GitHub URL: "
)

docs = load_repository(
    repo_url
)

print(
    f"\nTotal Documents: {len(docs)}"
)

print("\n")

print("="*50)
print("FIRST DOCUMENT")
print("="*50)

print(
    docs[0].metadata
)

print("\n")

print(
    docs[0].page_content[:1000]
)

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
        f"\nTotal Chunks: {len(chunks)}"
    )

    print("\n")

    print("=" * 50)
    print("FIRST CHUNK")
    print("=" * 50)

    print(
        chunks[0].metadata
    )

    print("\n")

    print(
        chunks[0].page_content
    )