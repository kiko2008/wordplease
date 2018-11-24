from django.forms import ModelForm

from blogs.models import Blog
from posts.models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['blog', 'title', 'introduction', 'post_body', 'url_image', 'url_video', 'categorys', 'pub_date']
        labels = {'categorys': 'Categorias', 'pub_date': 'Fecha de publicación'}

    # Un usuario solo puede publicar posts en sus propios blogs
    def __init__(self, user_logged, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(user=user_logged)
