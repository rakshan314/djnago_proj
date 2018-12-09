from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from matchings.models import Member, Hobby
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

#from mainapp.templatetags.extras import display_message

# datetime library to get time for setting cookie
import datetime as D
import sys

appname = 'MatchXHobby'

### API View Sets - BEGIN ###
from rest_framework import viewsets
#from .serializers import ProfileSerializer, MemberSerializer
### API View Sets - END ###


# decorator that tests whether user is logged in
def loggedin(view):
    def mod_view(request):
        if 'username' in request.session:
            username = request.session['username']
            try: user = Member.objects.get(username=username)
            except Member.DoesNotExist: raise Http404('Member does not exist')
            return view(request, user)
        else:
            return render(request,'mainapp/not-logged-in.html',{})
    return mod_view

def home(request):
    context = { 'appname': appname }
    return render(request, 'matchings/home.html', context)

def signup(request):
    context = { 'appname': appname }
    return render(request,'matchings/signup.html',context)

def register(request):
    if 'username' in request.POST and 'password' in request.POST:
        u = request.POST['username']
        p = request.POST['password']
        user = Member(username=u)
        user.set_password(p)
        try: user.save()
        except IntegrityError: raise Http404('Username '+u+' already taken: Usernames must be unique')
        context = {
            'appname' : appname,
            'username' : u
        }
        return render(request,'matchings/user-registered.html',context)

    else:
        raise Http404('POST data missing')


def login(request):
    return render(request, 'matchings/login.html')
