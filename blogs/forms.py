from django.contrib.auth.models import User
from django.forms import ModelForm

from blogs.models import Blog


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'user']
        labels = {'titulo': 'descripción'}

    # Un usuario solo puede crear sus propios blogs
    def __init__(self, user_logged, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(id=user_logged.id)
