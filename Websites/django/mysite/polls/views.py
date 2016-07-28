from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("YOU'RE AT THE POLLS INDEX.")

# Create your views here.
