from django.shortcuts import render
from django.views import View

from posts.models import Post


class HomeView(View):

    def get(self, request):
        last_posts_published = Post.objects.filter(status=Post.PUBLISHED).order_by('-pub_date')
        return render(request, 'home.html', {'list_last_published_posts': last_posts_published[:10]})
