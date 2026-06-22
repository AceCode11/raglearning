from clone_repo import clone_repository
from scanner import scan_repository
from summary import generate_summary


repo_url = input(
    "Enter GitHub Repository URL: "
)

repo_path = clone_repository(
    repo_url
)

files = scan_repository(
    repo_path
)

summary = generate_summary(
    repo_path,
    files
)

print("\n")
print("=" * 50)
print("REPOSITORY SUMMARY")
print("=" * 50)

print(f"\nRepository Name: {summary['repository_name']}")

print(f"\nTotal Files: {summary['total_files']}")

print("\nFile Types:")

for ext, count in summary["file_types"].items():

    print(f"{ext} : {count}")

print("\nFolders:")

for folder in summary["folders"]:

    print(f"- {folder}")