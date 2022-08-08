from cgitb import strong
from multiprocessing import context
from django.shortcuts import render
from github import Github

g = Github("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")
repo = g.get_repo("Hossein-79/WalletManager")

def GetContents(repo_contents):
    for repo_item in repo_contents:
        if repo_item.type == "dir":
            extends = repo.get_contents(repo_item.path)
            repo_item.sub = GetContents(extends)
    return repo_contents

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def choose_repo_file(request):
    context = {}
    if request.method == 'GET':
        #get repo files
        contents = repo.get_contents("")
        context['repo'] = GetContents(contents)
        print(context)
        return render(request, 'repository.html', context)
    
    if request.method == 'POST':
        #chek file
        return render(request, 'chose_contract.html', context)