from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("<center>Welcome to my weblog</center>")