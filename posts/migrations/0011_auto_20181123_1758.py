# Generated by Django 2.1.3 on 2018-11-23 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_url_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorys_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorys', models.ManyToManyField(through='posts.Post', to='posts.Category')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categorys_post',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='posts.Categorys_Post'),
            preserve_default=False,
        ),
    ]
