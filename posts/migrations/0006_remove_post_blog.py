# Generated by Django 2.1.3 on 2018-11-18 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blog',
        ),
    ]
