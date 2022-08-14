from django.shortcuts import render
from django.http import JsonResponse
from . import github
from . import algo_explorer

#test pages
def test1(request):
    return render(request, 'test1.html')

def test2(request):
    return render(request, 'test2.html')

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def choose_repo_file(request):
    context = {}
    if request.method == 'GET':
        #get repo files
        repo_url = request.GET.get('repo','')

        print(context)

        return JsonResponse(context)

def check_application(request):
    context = {}
    return render(request, 'check_application.html', context)

def search_application(request):
    #552635992
    app_id = request.GET.get('app_id','')
    context = algo_explorer.get_application_by_id(app_id)
    return render(request, 'search_application.html', context)