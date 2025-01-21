import os
import requests
from datetime import datetime

# Configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # Set your GitHub token as an environment variable
REPO_OWNER = 'your_username'  # Replace with your GitHub username or organization
REPO_NAME = 'your_repo_name'  # Replace with your repository name
CHANGELOG_FILE = 'CHANGELOG.md'

# GitHub API URL
GITHUB_API_URL = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls'

# Headers for GitHub API
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Categories based on labels
CATEGORIES = {
    'feature': '## 🚀 New Features',
    'bug': '## 🐛 Bug Fixes',
    'enhancement': '## ✨ Enhancements',
    'documentation': '## 📚 Documentation',
    'other': '## 🛠 Other Changes'
}

def fetch_merged_pull_requests():
    """Fetch merged pull requests from the GitHub API."""
    params = {
        'state': 'closed',
        'sort': 'updated',
        'direction': 'desc',
        'per_page': 100  # Adjust based on the number of PRs you expect
    }
    response = requests.get(GITHUB_API_URL, headers=headers, params=params)
    response.raise_for_status()
    pull_requests = response.json()
    return [pr for pr in pull_requests if pr['merged_at'] is not None]

def categorize_changes(pull_requests):
    """Categorize changes based on labels or PR descriptions."""
    changes = {category: [] for category in CATEGORIES.keys()}
    
    for pr in pull_requests:
        labels = [label['name'] for label in pr['labels']]
        title = pr['title']
        number = pr['number']
        url = pr['html_url']
        
        # Determine the category based on labels
        category = 'other'
        for label in labels:
            if label in CATEGORIES:
                category = label
                break
        
        # Add the change to the appropriate category
        changes[category].append(f"- {title} [#{number}]({url})")
    
    return changes

def update_changelog(changes):
    """Update the CHANGELOG.md file with the new changes."""
    today = datetime.now().strftime('%Y-%m-%d')
    new_changelog_entry = f"## {today}\n\n"
    
    for category, items in changes.items():
        if items:
            new_changelog_entry += f"{CATEGORIES[category]}\n"
            new_changelog_entry += "\n".join(items) + "\n\n"
    
    # Read the existing changelog
    with open(CHANGELOG_FILE, 'r') as file:
        existing_changelog = file.read()
    
    # Prepend the new changes to the existing changelog
    updated_changelog = new_changelog_entry + existing_changelog
    
    # Write the updated changelog back to the file
    with open(CHANGELOG_FILE, 'w') as file:
        file.write(updated_changelog)

def main():
    """Main function to update the changelog."""
    pull_requests = fetch_merged_pull_requests()
    changes = categorize_changes(pull_requests)
    update_changelog(changes)
    print("Changelog updated successfully!")

if __name__ == '__main__':
    main()