# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect

from accounts.forms import LoginForm


@csrf_protect
def app_login(request, template_name='accounts/login2.html'):
    context = RequestContext(request)
    title = 'Login Page'
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            if user.is_staff:
                return HttpResponseRedirect('/admin/')
            else:
                return HttpResponseRedirect(reverse_lazy('dashboard'))
        else:
            messages.error(request, 'Wrong Username or Password')
    else:
        form = LoginForm()
    return render(request, template_name, locals(), context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('index'))
