# Generated by Django 3.1.7 on 2021-03-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
