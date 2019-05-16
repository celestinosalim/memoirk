from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'memoirk_blog/home.html', context) 


def about(request):
    return render(request,"memoirk_blog/about.html", {'title': 'About'})