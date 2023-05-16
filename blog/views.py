from django.shortcuts import render
from .models import Post,Category
from django.shortcuts import get_object_or_404
# Create your views here.

def main_view (request):
    post = Post.objects.filter(status='published').order_by('-created')[:3]
    return render(request,'main/home.html',{'post':post  })


def post_view (request):
    post = Post.objects.filter(status='published').order_by('-created')
    return render(request,'blog/index.html',{'post':post  })

def post_detail(request,id_post):
    post = get_object_or_404(Post , id=id_post)
    return render (request,'blog/detail.html',{'post':post})