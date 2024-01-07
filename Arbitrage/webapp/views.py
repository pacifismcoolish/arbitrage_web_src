from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, msg):
    if msg is not None :
        result = 'you typed: "' + msg + '".'
    else: 
        result = 'Please type msg.'
    return HttpResponse(result)