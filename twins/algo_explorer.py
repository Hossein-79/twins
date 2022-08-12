import json
from multiprocessing import context
import requests

def get_application_by_id(app_id):
    r = requests.get(f'https://algoindexer.algoexplorerapi.io/v2/applications/{app_id}')
    obj = json.loads(r.text)
    context = {}
    print(r.status_code)
    if r.status_code == 200:
        if 'application' in obj:
            context['exist'] = True
            context['application'] = obj['application']
        else:
            context['exist'] = False
            context['message'] = obj['message']
    else:
        context['exist'] = False
        context['message'] = obj['message']
    return context
    
