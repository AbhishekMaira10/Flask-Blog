from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Abhishek Maira',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 17 2020'
    },
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 18 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
