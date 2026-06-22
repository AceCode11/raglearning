import os


def scan_repository(repo_path):

    files = []

    for root, dirs, filenames in os.walk(repo_path):

        dirs[:] = [

            d

            for d in dirs

            if d not in [
                ".git",
                "__pycache__",
                "node_modules",
                ".venv",
                "venv"
            ]
        ]

        for file in filenames:

            file_path = os.path.join(
                root,
                file
            )

            files.append(file_path)

    return files