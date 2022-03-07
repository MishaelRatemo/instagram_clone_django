from multiprocessing import context
import re
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib import  messages
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/accounts/login/')
def insta(request):
   context = {
      'title':'Instagram',
   }
   return render(request, 'index.html', context)

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/')