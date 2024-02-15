import argparse
from github import Github


def list_contributors(repo):
    contributors = repo.get_contributors()
    print("Contributors:")
    for contributor in contributors:
        print(contributor.login)


def check_files_existence(repo):
    try:
        security_md = repo.get_contents("SECURITY.md")
        print("SECURITY.md exists in the repository.")
    except:
        print("SECURITY.md does not exist in the repository.")

    try:
        issue_templates = repo.get_contents(".github/ISSUE_TEMPLATE")
        print("Issue templates exist:")
        for template in issue_templates:
            print(template.name)
    except:
        print("Issue templates do not exist in the repository.")


def check_repo_settings(repo):
    print(f"Repository '{repo.name}' Settings:")
    print(f"Default branch: {repo.default_branch}")
    print(f"Is private: {repo.private}")


def main():
    parser = argparse.ArgumentParser(description="GitHub Repository Management Script")
    parser.add_argument('-t', '--token', required=True, help="GitHub Personal Access Token")
    parser.add_argument('-u', '--username', required=True, help="GitHub Username")
    parser.add_argument('-r', '--repo', required=True, help="GitHub Repository Name")
    parser.add_argument('-c', '--contributors', action='store_true', help="List Contributors")
    parser.add_argument('-f', '--files', action='store_true', help="Check for SECURITY.md and Issue Templates")
    parser.add_argument('-s', '--settings', action='store_true', help="Check Repository Settings")
    args = parser.parse_args()

    if args.branch:
        get_branch_protection(args.username, args.repo,args.token)
    else:
        g = Github(args.token)
        repo = g.get_repo(f"{args.username}/{args.repo}")
    if args.contributors:
        list_contributors(repo)
    if args.files:
        check_files_existence(repo)
    if args.settings:
        check_repo_settings(repo)
    if args.actions:
        list_github_actions_workflows(repo)

    # Conceptual Note for Dependency Scanning and Security Alerts:
    print("Note: Dependency Scanning and Security Alerts are not directly accessible via PyGithub.")
    print("Please use GitHub's UI or the GitHub API with appropriate permissions for these checks.")


if __name__ == "__main__":
    main()
