from django.shortcuts import render

def index(request):
    return render(request, 'publication/index.html')