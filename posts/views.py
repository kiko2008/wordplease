from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView

from posts.forms import PostForm
from posts.models import Post


class HomeView(ListView):

    template_name = 'home.html'
    queryset = Post.objects.select_related('blog').filter(pub_date__lte=datetime.now()).order_by('-pub_date')[:10]
    context_object_name = 'list'


class PostDetailView(DetailView):

    model = Post
    template_name = 'detail_post.html'


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        post_form = PostForm(request.user)
        return render(request, 'new_post.html', {'form': post_form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Post()
        post_form = PostForm(request.user, request.POST, request.FILES, instance=new_post)
        if  post_form.is_valid():
            new_post =  post_form.save()
            messages.success(request, 'El post {0} se ha creado corretamente!'.format(new_post.title))
            post_form = PostForm(request.user)
        return render(request, 'new_post.html', {'form':  post_form})
