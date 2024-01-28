from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    param = {
        'title': 'アービトラージツール',
        'msg': 'アービトラージツール開始',
        'goto': 'next',
    }
    return render()