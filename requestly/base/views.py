from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse


def SimpleView(request):
    return HttpResponse("This is a simple test ! Please refer to the backend")
