from django.shortcuts import render
from django.http import HttpResponse

def FrontEnd(request):
    return HttpResponse("Hello, Please check your frontend!!")


