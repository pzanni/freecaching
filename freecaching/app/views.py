# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import Geocache


def index(request):
    geocache = Geocache.objects.get(pk=2)
    return render(request, 'app/index.html', {'geocache': geocache})