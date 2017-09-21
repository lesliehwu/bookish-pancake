# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    response = 'placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    if request.method == 'POST':
        print '*' * 50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = 'test'
        print '*' * 50
        return redirect('/')
    else:
        return redirect('/')

def show(request, blog_num):
    response = 'placeholder to display blog ' + blog_num
    return HttpResponse(response)

def edit(request, blog_num):
    response = 'placeholder to edit blog ' + blog_num
    return HttpResponse(response)

def destroy(request, blog_num):
    return redirect('/blogs')

# Create your views here.
