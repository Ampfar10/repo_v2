import os
import sys
import github

YOUR_ACCESS_TOKEN = input("Please enter your github access token: ") 
client = github.GitHub(access_token=YOUR_ACCESS_TOKEN)


repos = client.repos.list()

print("Repositories:")
for i, repo in enumerate(repos):
    print(f"{i+1}: {repo.name}")

selected_indices = []
while True:
    selected_index = input("Enter the number of a repository you want to delete (press enter once you are done): ")
    if selected_index == "":
        break
    selected_indices.append(int(selected_index))

for i in selected_indices:
    selected_repo = repos[i-1]
    client.repos.delete(selected_repo.owner.login, selected_repo.name)
    print(f"Successfully deleted repository {selected_repo.name}")
