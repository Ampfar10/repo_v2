import os
import sys
import github

client = github.GitHub(access_token=YOUR_ACCESS_TOKEN)

# Next, get the list of repositories for the authenticated user
repos = client.repos.list()

# Print the names of the repositories
print("Repositories:")
for i, repo in enumerate(repos):
    print(f"{i+1}: {repo.name}")

# Prompt the user to select one or more repositories to delete
selected_indices = []
while True:
    selected_index = input("Enter the number of a repository you want to delete (or press enter to finish): ")
    if selected_index == "":
        break
    selected_indices.append(int(selected_index))

# Delete the selected repositories
for i in selected_indices:
    selected_repo = repos[i-1]
    client.repos.delete(selected_repo.owner.login, selected_repo.name)
    print(f"Successfully deleted repository {selected_repo.name}")
