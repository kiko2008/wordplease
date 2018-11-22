from django.views.generic import ListView, DetailView

from blogs.models import Blog
from posts.models import Post


class BlogsView(ListView):

    template_name = 'blogs.html'
    queryset = Blog.objects.select_related('user').all()
    context_object_name = 'list_all_blogs'


class BlogDetailView(DetailView):

    model = Blog
    template_name = 'detail_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_posts'] = Post.objects.filter(blog_id = context.get('object').id).order_by('pub_date')
        return context

