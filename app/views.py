from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import generics,authentication,viewsets,permissions

from .models import Post,Comment
from .forms import PostForm,CommentForm
from .serializer import PostSerializer,CommentSerializer

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog_post.html'
    queryset = Post.objects.order_by('-pub_date')
    paginate_by = 2


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    comment=post.comment_set.all()
    forms=CommentForm
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.title = post
            print comment
            comment.save()
        else:
          print form.errors
    else:
        form = PostForm()

    return render(request, "blog_detail.html", {'form':forms,'post': post,'comment':comment})


def add_post(request):
    forms = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        print form
        if form.is_valid():

            form.save()
            return redirect("home")
        else:
          print form.errors
    else:
        form = PostForm()
    return render(request, "add_post.html", {'forms': forms})


def edit_post(request,slug):
    post=Post.objects.get(slug=slug)
    form = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        print form
        if form.is_valid():
            uncommit = form.save(commit=False)
            title= form.cleaned_data['title']
            description=form.cleaned_data['description']
            form.save()
            return redirect("home")
        else:
          print form.errors
    else:
        form = PostForm()
    return render(request, "edit_post.html", {'post':post,'form':form})

def delete_post(request,slug):
    posts=Post.objects.get(slug=slug)
    if request.method == 'POST':
        posts.delete()
        return redirect("home")

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
#
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer