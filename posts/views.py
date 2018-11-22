from django.contrib import messages
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from posts.forms import PostForm
from posts.models import Post


class HomeView(ListView):

    template_name = 'home.html'
    queryset = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')[:10]
    context_object_name = 'list_posts'


class PostDetailView(DetailView):

    model = Post
    template_name = 'detail_post.html'


class NewPostView(View):

    #@method_decorator(login_required)
    def get(self, request):
        post_form = PostForm()
        return render(request, 'new_post.html', {'form': post_form})

    #@method_decorator(login_required)
    def post(self, request):
        new_post = Post()
        post_form = PostForm(request.POST, request.FILES, instance=new_post)
        if  post_form.is_valid():
            new_post =  post_form.save()
            messages.success(request, 'El post {0} se ha creado corretamente!'.format(new_post.title))
            post_form = PostForm()
        return render(request, 'new_post.html', {'form':  post_form})
