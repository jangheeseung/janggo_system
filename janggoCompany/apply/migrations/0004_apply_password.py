# Generated by Django 2.1.5 on 2019-02-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0003_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='password',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]