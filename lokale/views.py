# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from django.template.loader import get_template
from lokale.forms import ClientRegistrationForm
from lokale.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from datetime import timedelta
from datetime import date
from django.db.models import Q
from django.core.mail import send_mail


def home(request): 
     all_entries = list(Juego.objects.all()[:5]) 
     return HttpResponse(render_to_response( 
                                         'index.html',{'page':'main_page.html','user':request.user, 'car_entry':all_entries}, 
                                         )) 


def view_profile(request):
    if(request.method == 'POST'):
        haslop = request.POST.get('cont','')
        mailp = request.POST.get('email','') 
        klient = Client.objects.get(nick = request.user.username)
        klient.cont = haslop
        klient.email = mailp
        klient.save()
        user = User.objects.get(username = request.user.username)
        user.email = mailp
        user.set_password(haslop)
        user.save()
        return HttpResponseRedirect('/register_success')
    req_user = request.user.username
    cur_user = Client.objects.get(nick=req_user)
    client_entries = Protokol.objects.filter(klient_id = cur_user)
    owner_entries = Protokol.objects.filter(wlasciciel_id = cur_user)
    c ={'page':'view_profile.html', 'user':request.user,'owner_entry':owner_entries,'client_entry':client_entries}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def login(request):
    c = {'page':'login.html', 'user':request.user}
    c.update(csrf(request))
    return HttpResponse(render_to_response('index.html',c))

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/login_me')
    else:
        return HttpResponseRedirect('/invalid')

def login_user(request):
    return HttpResponse(render_to_response('index.html',
                              {'page':'main_page.html','user': request.user}))

def logout_user(request):
    auth.logout(request)
    return render_to_response('index.html',{'page':'main_page.html','user':request.user})

def invalid_login(request):
    return render_to_response('index.html',{'page':'invalid.html','user':request.user})


def register(request):
    if request.method == 'POST':  
        loginp = request.POST.get('login','')
        haslop = request.POST.get('cont','')
        mailp = request.POST.get('email','')         
        klient = Client(nick = loginp, cont = haslop, email = mailp)
        klient.save()
        user = User(username = loginp)
        user.set_password(haslop)
        user.save()
        return HttpResponseRedirect('/register_success')

    c = {'page': 'register.html', 'user': request.user}
    c.update(csrf(request))

    return render_to_response('index.html',c) 

def register_success(request):
    return render_to_response('index.html',{'page':'register_success.html','user':request.user})
