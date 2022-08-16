import json
from multiprocessing import context
from unittest import result
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
    
def compile_teal(contract_file):
    r = requests.post('https://node.algoexplorerapi.io/v2/teal/compile/', data=contract_file, headers={'Content-Type':'text/plain'})
    obj = json.loads(r.text)
    return obj['result']
    