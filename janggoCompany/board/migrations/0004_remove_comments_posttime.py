# Generated by Django 2.1.5 on 2019-03-10 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_comments_posttime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='posttime',
        ),
    ]
