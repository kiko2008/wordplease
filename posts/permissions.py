from datetime import datetime

import pytz
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from blogs.models import Blog


class PostPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        utc = pytz.UTC
        datetime_start = obj.pub_date
        datetime_end = utc.localize(datetime.now())
        blog = get_object_or_404(Blog, pk=obj.blog_id)
        return request.user.is_superuser or request.user == blog.user or view.action == 'retrieve' and datetime_start <= datetime_end
