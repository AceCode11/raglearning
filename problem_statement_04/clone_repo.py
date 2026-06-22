from git import Repo
import os



def clone_repository(repo_url):
    repo_name = repo_url.split('/')[-1]

    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]

    local_path = os.path.join("repos" , repo_name)

    if os.path.exists(local_path):
        print("repository already exists")

        return local_path
    
    Repo.clone_from(
        repo_url , 
        local_path
    )

    print("repo clone completed successfully")

    return local_path