from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
#    return render('/test','test.html')
    return HttpResponse("You are in my world!")