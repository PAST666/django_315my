# Generated by Django 5.0.6 on 2024-07-31 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_blog', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]