# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Geocache, Profile

admin.site.register(Geocache)
admin.site.register(Profile)