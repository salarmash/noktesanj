# Generated by Django 5.1 on 2024-08-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceApp', '0003_rename_title_faq_title_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='Service', verbose_name='ویدئو'),
        ),
    ]
