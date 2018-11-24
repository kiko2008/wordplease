from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView

from blogs.forms import BlogForm
from blogs.models import Blog
from posts.models import Post, Category


class BlogsView(ListView):

    template_name = 'blogs.html'
    queryset = Blog.objects.select_related('user').all()
    context_object_name = 'list_all_blogs'


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'detail_blog.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        filter_category = self.request.GET.get('filter_category', None)
        if filter_category is None or filter_category == 'Elige una opcion...':
            list_posts = Post.objects.filter(blog_id=context.get('object').id).order_by('pub_date')
        else:
            list_posts = Post.objects.filter(blog_id=context.get('object').id, categorys = filter_category).order_by('pub_date')

        page = self.request.GET.get('page')

        paginator = Paginator(list_posts, 5)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context['list'] = posts
        context['categorys'] = Category.objects.all()
        return context


class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        blog_form = BlogForm(request.user)
        return render(request, 'new_blog.html', {'form': blog_form})

    @method_decorator(login_required)
    def post(self, request):
        new_blog = Blog()
        blog_form = BlogForm(request.user, request.POST, request.FILES, instance=new_blog)
        if  blog_form.is_valid():
            new_blog = blog_form.save()
            messages.success(request, 'El blog {0} se ha creado corretamente!'.format(new_blog.title))
            blog_form = BlogForm(request.user)
        return render(request, 'new_blog.html', {'form':  blog_form})
