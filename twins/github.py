from github import Github

g = Github("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")

def extend_repo(repo_contents, repo):
    for repo_item in repo_contents:
        if repo_item.type == "dir":
            extends = repo.get_contents(repo_item.path)
            repo_item.sub = extend_repo(extends, repo)
    return repo_contents

def get_repo(repo_url, repo_path):
    repo = g.get_repo(repo_url)
    contents = repo.get_contents(repo_path)
    # return extend_repo(contents, repo)
    context = {
        'full_name' : repo.full_name,
        'files' : contents
    }
    return context