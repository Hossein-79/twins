from multiprocessing import context
from github import Github

g = Github("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")

def extend_repo(repo_contents, repo):
    program_files = []
    for repo_item in repo_contents:
        if repo_item.type == "dir":
            extends = repo.get_contents(repo_item.path)
            program_files += extend_repo(extends, repo)

        if repo_item.path.lower().endswith(('.teal')):
            program_files.append(repo_item.path)
            
    return program_files

def get_repo(repo_url):
    context = {}
    try:
        repo = g.get_repo(repo_url)
        contents = repo.get_contents('')
        context ['full_name'] = repo.full_name
        context['files'] = extend_repo(contents, repo)
        context['success'] = True
    except:
        context['success'] = False
    return context