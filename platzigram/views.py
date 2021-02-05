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

def sort_integers(request): 
    """Return a JSON list  and sort a a list of number by get """
    #list comprehension
    numbers = sorted([int(i) for i in request.GET['numbers'].split(",")]) 
    data ={
        'status': 'ok',
        'numbers':numbers,
        'message': 'Integgers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name,age):
    """ return a greeting"""

    if age < 12 :
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Welcome {}'.format(name)

    return HttpResponse(message)