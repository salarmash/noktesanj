# Generated by Django 5.1 on 2024-08-26 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='short',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='کوتاه نوشت'),
        ),
    ]