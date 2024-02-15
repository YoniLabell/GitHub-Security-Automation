# GitHub-Security-Automation


This Python script is designed to manage various aspects of a GitHub repository, including listing contributors, checking for the existence of specific files (`SECURITY.md`, issue templates), examining repository settings, and listing GitHub Actions workflows. It also allows for the retrieval of branch protection settings for a specified branch.
# Repository Access Control Best Practices

## Principle of Least Privilege (PoLP)

Apply the Principle of Least Privilege to GitHub repositories to ensure users have the minimum access needed for their roles. This reduces risks like:

- **Accidental Exposure**: Limits chances of sensitive data leaks.
- **Malicious Attacks**: Decreases potential entry points for attackers.
- **Unintended Changes**: Reduces risk of accidental code alterations.

## GitHub Access Levels

GitHub offers several access levels:

- **Read**: View and fork the repository.
- **Triage**: Manage issues and pull requests without code access.
- **Write**: Contribute to the repository directly.
- **Maintain**: Manage repository without full admin rights.
- **Admin**: Full access to the repository, including settings and integrations.

## Best Practices

- Assign the **least amount of access** necessary.
- Review and adjust permissions as needed.

Remember, starting with minimal access and adjusting as necessary helps maintain security and integrity of your codebase.
## Prerequisites

- Python 3.x
- `PyGithub` library

## Installation

Before running the script, ensure you have Python 3 installed on your system. You can then install the required Python libraries using pip:

```bash
pip install requests PyGithub
```

## Configuration

To use this script, you need a GitHub Personal Access Token with the appropriate permissions to access repository information. You can generate a token by following the instructions in the GitHub documentation: [Creating a personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Usage

The script supports several command-line arguments to specify the operations you want to perform. Here's how you can use it:

```bash
python github_repo_management.py -t YOUR_GITHUB_TOKEN -u YOUR_USERNAME -r REPOSITORY_NAME [OPTIONS]
```

### Command-Line Arguments

- `-t` or `--token`: Your GitHub Personal Access Token (required).
- `-u` or `--username`: Your GitHub Username (required).
- `-r` or `--repo`: The GitHub Repository Name you wish to manage (required).
- `-c` or `--contributors`: List contributors of the repository.
- `-f` or `--files`: Check for the existence of `SECURITY.md` and issue templates.
- `-s` or `--settings`: Check repository settings.


### Examples

List contributors of a repository:

```bash
python github_repo_management.py -t YOUR_GITHUB_TOKEN -u YOUR_USERNAME -r REPOSITORY_NAME -c
```

Check for the existence of `SECURITY.md` and issue templates:

```bash
python github_repo_management.py -t YOUR_GITHUB_TOKEN -u YOUR_USERNAME -r REPOSITORY_NAME -f
```
## example
>github_checks.py --token github_pat_***** --username YoniLabell --repo GitHub-Security-Automation --settings
output:
Repository 'GitHub-Security-Automation' Settings:
Default branch: main
Is private: False



>github_checks.py --token github_pat_***** --username YoniLabell --repo GitHub-Security-Automation --contributors
output:
Contributors:
YoniLabell


>github_checks.py --token github_pat_***** --username YoniLabell --repo GitHub-Security-Automation --files
output:
SECURITY.md does not exist in the repository.
Issue templates do not exist in the repository.


## Note

Dependency scanning and security alerts are not directly accessible via this script. Please use GitHub's UI or the GitHub API with appropriate permissions for these checks.
