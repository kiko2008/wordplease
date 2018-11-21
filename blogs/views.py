from django.shortcuts import render
from django.views import View

from blogs.models import Blog


class BlogsView(View):

    def get(self, request):
        all_blogs = Blog.objects.select_related('user').all()

        return render(request, 'blogs.html', {'list_all_blogs': all_blogs})
