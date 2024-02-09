from django.shortcuts import render, HttpResponse

# Create your views here.


def index(requests):
    return HttpResponse("Hello This is Home Page")


def update_server(requests):
    return HttpResponse("Server Updated")