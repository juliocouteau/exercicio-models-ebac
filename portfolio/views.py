from django.shortcuts import render
from .models import Post

def post_view(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'portfolio/index.html', {'posts': posts})