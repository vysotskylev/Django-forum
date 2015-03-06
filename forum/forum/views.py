
from django.shortcuts import render_to_response

from django.http import HttpResponseRedirect

from django.contrib import auth

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/forum")
        else:
            return render_to_response('login.html', {'errors': 'Wrong login or username'})
    else:
        return render_to_response('login.html')

def logout(request):
    return render_to_response('logout.html')

def forum(request):
    return render_to_response('forum.html')
