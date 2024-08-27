# Generated by Django 5.1 on 2024-08-26 12:51

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=255, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'تنظیم عنوان',
                'verbose_name_plural': 'تنظیم عنوان',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=255, verbose_name='نام نویسنده')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name=' یوزر')),
            ],
            options={
                'verbose_name': 'نویسنده',
                'verbose_name_plural': 'نویسندگان',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='تصویر مطلب')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان بلاگ')),
                ('short', models.CharField(blank=True, max_length=255, null=True, verbose_name='نقل قول')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('content1', tinymce.models.HTMLField(verbose_name='متن بخش اول')),
                ('content2', tinymce.models.HTMLField(blank=True, null=True, verbose_name='متن بخش دوم')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='BlogApp.author', verbose_name='نویسنده')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='BlogApp.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مطلب',
                'verbose_name_plural': 'بلاگ ها',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blog', verbose_name='تصویر ')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='BlogApp.post')),
            ],
            options={
                'verbose_name': 'نگاره',
                'verbose_name_plural': 'گالری',
            },
        ),
    ]