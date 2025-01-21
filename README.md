# Automated Changelog Updater

A tool to automatically update your `CHANGELOG.md` file based on merged pull requests. It categorizes changes using GitHub labels or PR descriptions and appends them to the changelog in a structured format.

## Features

- Fetches merged pull requests from your GitHub repository.
- Categorizes changes based on labels (e.g., `feature`, `bug`, `enhancement`, `documentation`).
- Updates the `CHANGELOG.md` file with new changes in a standardized format.
- Easy to integrate into your CI/CD pipeline.

## Prerequisites

- Python 3.7 or higher.
- A GitHub Personal Access Token (PAT) with `repo` access.
- A `CHANGELOG.md` file in your repository (can be empty or pre-existing).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/your_repo_name.git
   cd your_repo_name
   ```

2. Install the required Python packages:
   ```bash
   pip install requests
   ```

3. Set your GitHub token as an environment variable:
   ```bash
   export GITHUB_TOKEN='your_github_token'
   ```

## Usage

1. Update the configuration in the script:
   - Replace `your_username` and `your_repo_name` in the `REPO_OWNER` and `REPO_NAME` variables with your GitHub username and repository name.

2. Run the script:
   ```bash
   python changelog_updater.py
   ```

3. Check your `CHANGELOG.md` file for updates. The script will append new changes under the appropriate categories.

### Example Output

After running the script, your `CHANGELOG.md` file might look like this:

```markdown
## 2023-10-15

### 🚀 New Features
- Added user authentication [#123](https://github.com/your_username/your_repo_name/pull/123)
- Implemented dark mode [#124](https://github.com/your_username/your_repo_name/pull/124)

### 🐛 Bug Fixes
- Fixed login page crash [#125](https://github.com/your_username/your_repo_name/pull/125)

### ✨ Enhancements
- Improved API response time [#126](https://github.com/your_username/your_repo_name/pull/126)

### 📚 Documentation
- Updated README file [#127](https://github.com/your_username/your_repo_name/pull/127)

### 🛠 Other Changes
- Updated dependencies [#128](https://github.com/your_username/your_repo_name/pull/128)
```

## Configuration

You can customize the script by modifying the following:

- **Categories**: Update the `CATEGORIES` dictionary in the script to match the labels used in your repository.
- **Changelog Format**: Modify the `update_changelog` function to change the format of the changelog entries.

## Integrating with CI/CD

You can integrate this tool into your CI/CD pipeline to automatically update the changelog whenever a pull request is merged. For example, in GitHub Actions:

```yaml
name: Update Changelog

on:
  pull_request:
    types:
      - closed

jobs:
  update-changelog:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install requests

      - name: Run Changelog Updater
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python changelog_updater.py

      - name: Commit and push changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add CHANGELOG.md
          git commit -m "Update CHANGELOG.md"
          git push
```

## Contributing

Contributions are welcome! If you'd like to improve this tool, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
