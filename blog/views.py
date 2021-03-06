from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import request
from django.shortcuts import render
from django.template import Template , Context, context
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import post
# Create your views here.


def home(request):
    posts = post.objects.all()
    context = {
        "posts": posts
    }
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model=post
    template_name= 'blog/home.html' #<app>/<model>_<viewtype>.html  template given 
    context_object_name= 'posts'
    ordering = '-date_posted'

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# dcfaes