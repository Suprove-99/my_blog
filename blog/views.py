from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Posts

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomepageView(ListView):
    model = Posts
    template_name = 'home.html'


class PostDetailsView(DetailView):
    model = Posts
    template_name = 'details.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name = 'create.html'
    fields = '__all__'


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Posts
    template_name = 'update.html'
    fields = ['title', 'body']


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class AboutView(TemplateView):
    template_name = 'about.html'