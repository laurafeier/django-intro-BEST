from django.shortcuts import render
from django.http import HttpResponse


def greeter(request):
    return HttpResponse("Hello light! Where's my HTML??")