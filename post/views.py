from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone

def post_list(request):
    return render(request, 'blog/post_list.html',{})

# Create your views here.
def index(request):
    posts = Post.objects.filter(date_updated__lte=timezone.now()).order_by('date_updated')
    return render(request, 'index.html',{})
