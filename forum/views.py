from django.shortcuts import render, redirect
from django.views import View
# Create your views here.

def forums(request):
    return render(request, 'forum/forums.html')


def detail(request):
    return render(request, 'forum/detail.html')

    
def posts(request):
    return render(request, 'forum/posts.html')