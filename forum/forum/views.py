
from django.shortcuts import render_to_response

def login(request):
    return render_to_response('login.html')

def logout(request):
    return render_to_response('logout.html')

def forum(request):
    return render_to_response('forum.html')
