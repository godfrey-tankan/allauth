from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_view(request):
    if not request.user.is_authenticated:
        return render(request, 'landing.html')
    return render(request, 'home.html')