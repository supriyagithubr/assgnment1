# Generated by Django 4.2 on 2023-04-26 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_published_date_alter_blog_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
