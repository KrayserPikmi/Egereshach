from django.shortcuts import render


def index(request):
    return render(request, "main/index.html")


def socialstudies(request):
    return render(request, "main/socialstudies.html")