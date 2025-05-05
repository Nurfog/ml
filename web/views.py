from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
from django.middleware.csrf import get_token
#from cms.forms import PaisForm




def index(request):
    return render(request, 'web/pages/index.html')

def about(request):
    return render(request, 'web/pages/about.html')

def courses(request):
    return render(request, 'web/pages/courses.html')

def team(request):
    return render(request, 'web/pages/team.html')

def contact(request):
    return render(request, 'web/pages/contact.html')

def blog(request):
    return render(request, 'web/pages/blog.html')

def testimonial(request):
    return render(request, 'web/pages/testimonial.html')

def error_404(request):
    return render(request, 'web/pages/404.html', status=404)

def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

#def login(request):
#    return render(request, 'autenticacion/account/login.html')

