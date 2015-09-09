from django.shortcuts import render

# Create your views here.
# Dev: Rohan
# Date: 09/08/2015

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
