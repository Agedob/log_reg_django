from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt

def index(request):
    if Users.objects.filter(first_name__contains="test"):
        bye = Users.objects.get(first_name="test")
        bye.delete()
    return render(request,'login/index.html',{'Users':Users.objects.all()})

def regi(request):
    if request.method != 'POST':
        messages.error(request, "Create User")
        return redirect('/')
    else:
        errors = Users.objects.simple_validator(request.POST)
        if len(errors):
            for key,values in errors.iteritems():
                messages.success(request, values)
            return redirect('/')
        else:
            email = request.POST['email']
            me = Users.objects.get(email=email)
            request.session['id'] = me.id
            return redirect('/done')

def login(request):
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for key,values in errors.iteritems():
            messages.success(request, values)
        return redirect('/')
    else:
        id = Users.objects.get(email=request.POST['email']).id
        request.session['id'] = id
        return redirect('/done')

def done(request):
    return render(request, 'login/done.html')
