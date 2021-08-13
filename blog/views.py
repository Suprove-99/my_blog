from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts


# Create your views here.
class HomepageView(ListView):
    model = Posts
    template_name = 'home.html'


class PostDetailsView(DetailView):
    model = Posts
    template_name = 'details.html'


class CreatePostView(CreateView):
    model = Posts
    template_name = 'create.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'update.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
