# Generated by Django 2.1.5 on 2019-03-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='posttime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
