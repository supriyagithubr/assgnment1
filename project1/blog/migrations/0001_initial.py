# Generated by Django 4.2 on 2023-04-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=60)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
