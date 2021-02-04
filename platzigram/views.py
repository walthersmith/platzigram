"""Platzigram Views"""
#Django
import json
from django.http import HttpResponse
#Utilities
from datetime import datetime 

def hello_world(request):
    """return hello world"""
    #now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! current server time is {now} '.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')))

def hi(request): 
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    numbers.sort()
    return HttpResponse(json.dumps(numbers))

