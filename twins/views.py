import json
import os
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from . import github
from . import algo_explorer
from .models import Application

# Create your views here.
def index(request):
    applications = Application.objects.all().filter(expired=False).order_by('-id')[:3]
    context = {'applications': applications}
    return render(request, 'index.html', context)

def all_applications(request):
    applications = Application.objects.all().filter(expired=False).order_by('-id')
    context = {'applications': applications}
    return render(request, 'all_applications.html',context)

@csrf_exempt
def search_application(request):
    if request.method == 'POST':
        context = {}
        body = json.loads(request.body.decode('utf-8'))
        app_id = body['app_id']
        try:
            app = Application.objects.get(contract_id = app_id, expired=False)
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
            repo_path = '/'.join(repo_url.split('github.com/')[1].split('/')[0:2])
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
 
        app = algo_explorer.get_application_by_id(app_id)
        if app['exist'] == False:
            context['success'] = False
            return JsonResponse(context)

        if Application.objects.filter(contract_id = app_id, expired=False).exists():
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
            Application.objects.filter(contract_id = app_id, expired=True).delete()
            repo_owner , repo_name = repo_url.split('/')
            last_commit = github.get_last_commit_sha(repo_url)
            application = Application.objects.create(
                repository_name = repo_name,
                owner_name = repo_owner,
                contract_id = app['application']['id'],
                commit_hash = last_commit,
                expired = False,
                file_path = file_path,
            )

        return JsonResponse(context)

def get_application(request, app_id):
    context = {}
    try:
        app = Application.objects.get(contract_id = app_id)
        context['app'] = app

        last_hash = github.get_last_commit_sha(f'{app.owner_name}/{app.repository_name}')
        if app.commit_hash != last_hash:
            check_app = algo_explorer.get_application_by_id(app_id)
            approval_program = check_app['application']['params']['approval-program']
            program_string = github.get_contract_as_string(f'{app.owner_name}/{app.repository_name}', app.file_path)
            compiled = algo_explorer.compile_teal(program_string)
            print(compiled)
            if compiled == approval_program:
                app.expired = False
                app.commit_hash = last_hash
            else:
                app.expired = True
            app.save()

        if app.expired == True:
            return render(request, 'expired.html', context)

        return render(request, 'application.html', context)
    except:
        context['app_id'] = app_id
        return render(request, 'rejected.html', context)

def get_badge(request, app_id):
    path = ''
    try:
        app = Application.objects.get(contract_id = app_id)

        if app.expired == True:
            path = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'twins/media/expired.png')
        else:
            last_hash = github.get_last_commit_sha(f'{app.owner_name}/{app.repository_name}')
            if app.commit_hash != last_hash:
                check_app = algo_explorer.get_application_by_id(app_id)
                approval_program = check_app['application']['params']['approval-program']
                program_string = github.get_contract_as_string(f'{app.owner_name}/{app.repository_name}', app.file_path)
                compiled = algo_explorer.compile_teal(program_string)
                print(compiled)
                if compiled == approval_program:
                    app.expired = False
                    app.commit_hash = last_hash
                else:
                    app.expired = True
                app.save()

            if app.expired == False:
                path = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'twins/media/verified.png')
            else:
                path = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'twins/media/expired.png')
    except:
        path = os.path.join(os.path.dirname(os.path.dirname(__file__)), r'twins/media/invalid.png')
    
    img = open(path, 'rb')
    response = FileResponse(img)
    response.headers['Content-Type'] = 'image/png'
    return response

