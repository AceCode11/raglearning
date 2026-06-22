import os
from collections import Counter

def generate_summary(repo_path , files):
    repo_name = os.path.basename(repo_path)

    extensions = []

    folders = set()

    for file in files: 
        ext = os.path.splitext(file)[1]

        if ext:
            extensions.append(ext)


        relative_path = os.path.relpath(file , repo_path)

        folder_parts = relative_path.split(os.sep)
        


        if len(folder_parts) > 1:
            folders.add(folder_parts[0])

    extension_count = Counter(extensions)

    summary = {
        "repository_name": repo_name,
        "total_files": len(files),
        "file_types": dict(extension_count),
        "folders": sorted(list(folders))
    }

    return summary
