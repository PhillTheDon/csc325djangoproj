from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    submitted = False

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            submitted = True

    return render(request, 'myapp/contact.html', {
        'submitted': submitted
    })

@api_view(['GET'])
def api_home(request):
    data = {
        "message": "Welcome to my CSC325 Django API!",
        "project": "CSC325 CI/CD Project",
        "status": "running"
    }

    return Response(data)