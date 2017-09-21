# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def users(request):
    meep = 'placeholder to later display all the list of users'
    return HttpResponse(meep)

def new(request):
    deedle = 'placeholder for users to create a new user record'
    return HttpResponse(deedle)

def login(request):
    meep = 'placeholder for users to login'
    return HttpResponse(meep)
