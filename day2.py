import os
import git
import datetime

# Configuration
REPO_PATH = "/path/to/your/repo"  # Local path to your Git repository
COMMIT_MESSAGE = "Automated commit from script"
FILE_NAME = "auto_update.txt"     # File to update
GITHUB_USERNAME = "your-username"
GITHUB_ACCESS_TOKEN = "your-personal-access-token"
GITHUB_REPO_URL = f"https://{nischalsir}:{GITHUB_ACCESS_TOKEN}@github.com/{nischalsir}/python.git"

def make_changes():
    """Modify or create a file to simulate a change."""
    file_path = os.path.join(REPO_PATH, FILE_NAME)
    with open(file_path, "a") as f:
        f.write(f"Update on {datetime.datetime.now()}\n")

def push_changes():
    """Stage, commit, and push changes to GitHub."""
    try:
        # Load repository
        repo = git.Repo(REPO_PATH)
        if repo.is_dirty(untracked_files=True):
            # Stage changes
            repo.git.add(A=True)
            
            # Commit changes
            repo.index.commit(COMMIT_MESSAGE)
            
            # Push changes
            origin = repo.remote(name='origin')
            origin.push()
            print("Changes pushed successfully!")
        else:
            print("No changes to commit.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to automate the process."""
    if not os.path.exists(REPO_PATH):
        print("Invalid repository path.")
        return
    
    make_changes()
    push_changes()

if __name__ == "__main__":
    main()
