# Generated by Django 2.1.3 on 2018-11-24 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_auto_20181124_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url_video',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
