from cgitb import strong
from multiprocessing import context
from django.shortcuts import render
from . import github
from . import algo_explorer

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
        return render(request, 'choose_contract.html', context)

def check_application(request):
    context = {}
    return render(request, 'check_application.html', context)

def search_application(request):
    #552635992
    app_id = request.GET.get('app_id','')
    context = algo_explorer.get_application_by_id(app_id)
    return render(request, 'search_application.html', context)