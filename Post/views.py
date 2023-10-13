from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from django import forms
from .forms import PostForm


#
# # Create your views here.
# class PostListView(ListView):
#     model = Post
#     queryset = Post.objects.all()
#     template_name = 'posts/list_view.html'


def create_post(request,user):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user

            new_post = form.save(commit=False)
            new_post.user = user
            new_post.save()

            return redirect('profile', username=user)
    else:
        form = PostForm()

    return render(request, 'posts/post.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()  # You can adjust this query as needed
    return render(request, 'profile/profile.html', {'posts': posts})