import getpass
import github

# Prompt the user for their GitHub username and access token
username = input("Enter your GitHub username: ")
access_token = getpass.getpass("Enter your GitHub access token: ")

# Create a GitHub API client using the provided username and access token
client = github.Github(login_or_token=access_token, user=username)

# Next, get the list of repositories for the authenticated user
repos = client.get_user().get_repos()

# Print the names of the repositories
print("Repositories:")
for i, repo in enumerate(repos):
    print(f"{i+1}: {repo.name}")

# Prompt the user to select one or more repositories to delete
selected_indices = []
while True:
    choice = input("Enter the number of a repository you want to delete (or press enter to finish): ")
    if choice == "":
        break
    selected_indices.append(int(choice))

# Delete the selected repositories
for i in selected_indices:
    selected_repo = repos[i-1]
    selected_repo.delete()
    print(f"Successfully deleted repository {selected_repo.name}")
