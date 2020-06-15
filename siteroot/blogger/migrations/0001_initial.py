# Generated by Django 3.0.5 on 2020-06-14 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=80)),
                ('text', models.TextField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update timestamp')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogger.Blog')),
            ],
        ),
    ]
