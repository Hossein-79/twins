import json
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import github
from . import algo_explorer
from .models import Application

#test pages
def test1(request):
    return JsonResponse({'ss':'sss'})

def test2(request):
    return render(request, 'test2.html')

# Create your views here.
def index(request):
    applications = Application.objects.all().filter(expired=False)[:3]
    context = {'applications': applications}
    return render(request, 'index.html', context)

def all_applications(request):
    applications = Application.objects.all().filter(expired=False)
    context = {'applications': applications}
    return render(request, 'all_applications.html',context)

@csrf_exempt
def search_application(request):
    if request.method == 'POST':
        context = {}
        body = json.loads(request.body.decode('utf-8'))
        app_id = body['app_id']
        try:
            app = Application.objects.get(contract_id = app_id)
            context = {
                'success' : True , 
                'validated' : True,
                'app_id' : app.contract_id
            }
        except :
            context['validated'] = False

            app = algo_explorer.get_application_by_id(app_id)
            if app['exist'] == True:
                if app['application']['deleted'] == True:
                    context['success'] = False
                    context['message'] = 'application was deleted'

                context['success'] = True
                context['app_id'] = app['application']['id']
                context['creator'] = app['application']['params']['creator']
                context['create_block'] = app['application']['created-at-round']
            else:
                context['success'] = False
                context['message'] = app['message']
    return JsonResponse(context)

@csrf_exempt
def get_repo_contract_files(request):
    if request.method == 'POST':
        context = {}
        body = json.loads(request.body.decode('utf-8'))
        repo_url = body['github_repo']

        try:
            repo_path = repo_url.split('github.com/')[1]    
            context = github.get_repo(repo_path)
        except:
            context['success'] = False
            context['message'] = 'Url is invalid'

        return JsonResponse(context)

@csrf_exempt
def check_application(request):
    if request.method == 'POST':
        context = {}
        body = json.loads(request.body.decode('utf-8'))
        repo_url = body['github_repo']
        file_path = body['file_path']
        app_id = body['app_id']

        print(repo_url, file_path, app_id)

        app = algo_explorer.get_application_by_id(app_id)
        if app['exist'] == False:
            context['success'] = False
            return JsonResponse(context)

        approval_program = app['application']['params']['approval-program']

        program_string = github.get_contract_as_string(repo_url, file_path)
        if program_string is '':
            context['success'] = False
            return JsonResponse(context)

        compiled = algo_explorer.compile_teal(program_string)

        context['success'] = True
        context['app_id'] = app['application']['id']

        if compiled == approval_program:
            application = Application.objects.create()
            print('true')
        else:
            print('false')

        return JsonResponse(context)













def get_application(request, app_id):
    print(app_id)
    context = {}
    try:
        app = Application.objects.get(contract_id = app_id)
        context['app'] = app
        return render(request, 'application.html', context)
        #return JsonResponse({'validated' : True, 'app_id' : app.contract_id})
    except:
        return JsonResponse({'sdfs' : 'sdf'})

    # context = algo_explorer.get_application_by_id(app_id)
    # return render(request, 'search_application.html', context)

def choose_repo_file(request):
    context = {}
    if request.method == 'GET':
        #get repo files
        repo_url = request.GET.get('repo','')

        print(context)

        return JsonResponse(context)
