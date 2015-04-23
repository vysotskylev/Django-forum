
from django.shortcuts import render
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

from django.contrib import auth

from main.models import Message, Profile, Thread

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            return render(request, 'register.html',
                    {'errors': 'This username is already taken'})

        user = User.objects.create_user(username=username, password=password)
        profile = Profile.objects.create(user=user)
        profile.save()
        if user:
            user = auth.authenticate(username=username, password=password)
            auth.login(request,user)
            return HttpResponseRedirect("/threads")

        return render(request, str(user))
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/threads")
        else:
            return render(request, 'login.html', {'errors': 'Wrong login or username'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/threads")

def thread(request, threadName):
    thread = Thread.objects.get(name=threadName)
    if not thread:
        raise Exception("Thread {} doesn't exist".format(threadName))

    if request.method == 'POST':
        if request.user.is_authenticated():
            text = request.POST.get('text','')
            to = request.POST.get('to', '')
            print "TO: " + to
            if to == '':
                message = Message.objects.create(text = text, author = request.user, thread = thread)
            else:
                toUser = User.objects.get(username=to)
                message = Message.objects.create(text = text, author = request.user, to = toUser, thread = thread)

            message.save()
    messages = thread.message_set.all()

    return render(request, 'thread.html', {'thread_name': threadName, 'messages': messages})

def all_threads(request):
    if request.method == 'POST' and request.user.is_authenticated():
        #TODO return error instead of defaulting
        threadName = request.POST.get('threadName', 'Default thread')
        thread = Thread.objects.create(name=threadName)
        thread.save()
        return HttpResponseRedirect("/threads/{}".format(threadName))
    return render(request, 'forum.html', {'threads' : Thread.objects.all()})

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/threads')
    return HttpResponseRedirect('/login')

def personal_page(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            request.user.profile.signature = request.POST.get('signature', '')
            request.user.profile.save()
        return render(request, 'personal_page.html')
    return HttpResponseRedirect('/login')
