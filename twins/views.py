from cgitb import strong
from multiprocessing import context
from django.shortcuts import render
from . import github

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def choose_repo_file(request):
    context = {}
    if request.method == 'GET':
        #get repo files
        repo_url = request.GET.get('repo','')
        repo_path = request.GET.get('path','')

        context['repo'] = github.get_repo(repo_url, repo_path)

        return render(request, 'repository.html', context)
    
    if request.method == 'POST':
        #check file
        return render(request, 'chose_contract.html', context)