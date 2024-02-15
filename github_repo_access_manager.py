from github import Github, GithubException
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Manage GitHub repository access using PyGithub.')
parser.add_argument('--token', required=True, help='GitHub personal access token')
parser.add_argument('--owner', required=True, help='Repository owner username')
parser.add_argument('--repo', required=True, help='Repository name')
parser.add_argument('--username', help='Collaborator username')
parser.add_argument('--permission', choices=['pull', 'push', 'admin', 'maintain', 'triage'], help='Permission level for the collaborator')
parser.add_argument('--action', required=True, choices=['list', 'add', 'remove'], help='Action to perform: list, add, or remove collaborators')

args = parser.parse_args()

# Initialize Github instance
g = Github(args.token)

# Get repository
repo = g.get_repo(f"{args.owner}/{args.repo}")

def list_collaborators():
    for collaborator in repo.get_collaborators():
        print(collaborator.login)

def add_collaborator(username, permission):
    try:
        repo.add_to_collaborators(username, permission)
        print(f"Successfully added or updated {username} with {permission} permission.")
    except GithubException as e:
        print(f"Failed to add or update collaborator: {e.data}")

def remove_collaborator(username):
    try:
        repo.remove_from_collaborators(username)
        print(f"Successfully removed {username}.")
    except GithubException as e:
        print(f"Failed to remove collaborator: {e.data}")
def main():
    # Execute the appropriate function based on the action argument
    if args.action == 'list':
        list_collaborators()
    elif args.action == 'add' and args.username and args.permission:
        add_collaborator(args.username, args.permission)
    elif args.action == 'remove' and args.username:
        remove_collaborator(args.username)
    else:
        print("Invalid action or missing arguments.")
if __name__ == "__main__":
    main()
