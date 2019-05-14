from django.shortcuts import render

posts = [
    {
        'author': 'CelestinoS',
        "title": 'Blog Post 1',
        "content": 'First post',
        "date_posted": 'August 28 1029'
    },
    {
        'author': 'alexS',
        "title": 'Blog Post 2',
        "content": 'second post',
        "date_posted": 'August 28 1029'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'memoirk_blog/home.html', context) 


def about(request):
    return render(request,"memoirk_blog/about.html", {'title': 'About'})