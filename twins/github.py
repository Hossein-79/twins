from github import Github
import requests

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
        context['message'] = 'GitHub Repository is invalid'

    if not context['files']:
        context['success'] = False
        context['message'] = 'Repository does not contain any \'.teal\' files'

    return context

def get_last_commit_sha(repo_url):
    try:
        repo = g.get_repo(repo_url)
        commits = repo.get_commits()
        return commits[0].sha
    except:
        return ''

def get_contract_as_string(repo_url, repo_path):
    try:
        repo = g.get_repo(repo_url)
        file = repo.get_contents(repo_path)
        download_url = file.download_url
        r = requests.get(download_url)
        contract_file = r.text
        return contract_file
    except:
        return ''