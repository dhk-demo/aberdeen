from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from django_otp.decorators import otp_required

@otp_required
def forums(request):
    return render(request, 'forum/forums.html')

@otp_required
def detail(request):
    return render(request, 'forum/detail.html')

@otp_required    
def posts(request):
    return render(request, 'forum/posts.html')