from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    
    request.session['count'] += 1
    print 'count' in request.session
    
    context = {
            'word':get_random_string(length=14),
            'count':request.session['count']
    }

    if request.method == 'POST':
        return redirect

    
    return render(request, 'random_word/index.html',context)
