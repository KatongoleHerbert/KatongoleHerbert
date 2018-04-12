# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.urls import reverse_lazy

from accounts.forms import ChangePasswordForm
from collab.forms import ProjectForm, SearchForm
import datetime

from collab.models import Project, My_workables


def calc(x, y):
    s1 = str(x)
    s2 = str(y)
    FMT = '%H:%M:%S'
    tdelta = datetime.datetime.strptime(s2, FMT) - datetime.datetime.strptime(s1, FMT)
    z = re.findall(r'\d+', str(tdelta))
    y = z[0]
    return int(y)


@login_required
def index(request, template_name='collab/dashboard.html'):
    context = RequestContext(request)
    title = 'My Collabo'
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
        else:
            messages.error(request, "Passwords don't match")
    else:
        form = PasswordChangeForm(request.user)

    return render(request, template_name, locals(), context)


@login_required
def labs(request, template_name='collab/labs.html'):
    context = RequestContext(request)
    title = 'My Collabo'

    return render(request, template_name, locals(), context)


@login_required
def book_page(request, template_name='collab/book.html'):
    context = RequestContext(request)
    title = 'My Collabo'
    booked_times = Project.objects.filter(date=datetime.date.today(), booked=True)
    my_date = datetime.date.today()
    query = request.GET.get('q')

    if request.method == 'POST' and 'booking' in request.POST:
        form = ProjectForm(request.POST)
        if form.is_valid():
            submission = form.cleaned_data
            project_name = submission.get('project_name')
            date = submission.get('date')
            start_time = submission.get('start_time')
            end_time = submission.get('end_time')
            is_clear = Project.objects.filter(date=date, start_time=start_time, end_time=end_time).count()

            if request.user.is_authenticated():
                if calc(start_time, end_time) == 1:
                    if is_clear == 0:
                        instance = form.save(commit=False)
                        instance.user = request.user
                        instance.booked = True
                        instance.save()
                        HttpResponseRedirect(reverse_lazy('book'))
                        messages.success(request, 'Successfully submitted')
                    else:
                        messages.error(request, 'Time already booked')
                else:
                    messages.error(request, 'Time difference should be one hour')
        else:
            messages.error(request, 'Something went wrong during submission try again')
            HttpResponseRedirect(reverse_lazy('index'))
    else:
        form = ProjectForm()

    if query:
        booked_times = Project.objects.filter(date__contains=query, booked=True)
    return render(request, template_name, locals(), context)


def contact(request, template_name='collab/contact.html'):
    context = RequestContext(request)
    title = 'Contact us'
    return render(request, template_name, locals(), context)


def about(request, template_name='collab/about.html'):
    context = RequestContext(request)
    title = 'About us'
    return render(request, template_name, locals(), context)
