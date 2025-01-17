# Generated by Django 5.1 on 2024-08-26 10:43

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Team', verbose_name='نگاره')),
                ('name', models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')),
                ('role', models.CharField(max_length=100, verbose_name='پوزیشن شغلی')),
                ('content', tinymce.models.HTMLField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'فرد',
                'verbose_name_plural': 'تیم',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Team', verbose_name='آیکون')),
                ('title', models.CharField(max_length=100, verbose_name=' نام شبکه اجتماعی')),
                ('role', models.CharField(max_length=100, verbose_name='لینک شبکه اجتماعی')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='TeamApp.team')),
            ],
            options={
                'verbose_name': 'شبکه اجتماعی',
                'verbose_name_plural': 'شبکه های اجتماعی',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255, verbose_name='لیبل')),
                ('value', models.CharField(max_length=255, verbose_name='مقدار')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='TeamApp.team')),
            ],
            options={
                'verbose_name': 'آیتم',
                'verbose_name_plural': 'مشخصات فردی',
            },
        ),
    ]
