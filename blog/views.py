from django.shortcuts import render
from .models import Post,Category ,CommentPost
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect 
from django.urls import reverse , reverse_lazy
from django.contrib import messages
from .form import CommentForm
# Create your views here.

def main_view (request):
    post = Post.objects.filter(status='published').order_by('-created')[:3]
    return render(request,'main/home.html',{'post':post  })


def post_view (request):
    post = Post.objects.filter(status='published').order_by('-created')
    return render(request,'blog/index.html',{'post':post  })

def post_detail(request,pk):
    post = get_object_or_404(Post , id=pk)
    comment_form = CommentForm()
    comment = CommentPost.objects.filter(post=post.id).order_by('-created')[:10]
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
               email = request.POST['email']
               content = request.POST['content']
               new_comment = CommentPost.objects.create(post=post , user = request.user , email = email , content = content)
               new_comment.save()
               messages.success(request , 'Comment Added Successfully')
               return HttpResponseRedirect(request.path_info)
        else:
            messages.success(request , 'Please login or register')
            return HttpResponseRedirect(request.path_info)
    return render (request,'blog/detail.html',{'post':post , 'form':comment_form , 'comment':comment})

def post_like(request , post_id):
    post = get_object_or_404(Post , id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
        messages.success(request , 'Post Unliked')
        return HttpResponseRedirect(reverse('post_detail' , args=[post_id]))
    else:
        post.likes.add(request.user)
        messages.success(request , 'Post liked')
        return HttpResponseRedirect(reverse('post_detail' , args=[post_id]))