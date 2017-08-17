from django.shortcuts import render

def index(request):
    return render(request, 'recontact/index.html', {})
