# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def registration(request):
    return render(request, 'registration.html', {})
