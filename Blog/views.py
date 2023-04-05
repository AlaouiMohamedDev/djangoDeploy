from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    """
    posts=[
     {'title': 'Python for Beginners',
      'content': 'A beginner-friendly guide to learning Python programming language.',
       'pub_date': '2021-01-01'},
       {'title': 'Python Cookbook',
        'content': 'A collection of Python recipes for solving common problems.',
        'pub_date': '2022-02-15'},
        {'title': 'Python Data Science Handbook',
         'content': 'A comprehensive guide to data science with Python.', 
         'pub_date': '2020-03-28'}
       
       ]"""
    return render(request, 'post_list.html', {'posts': posts})