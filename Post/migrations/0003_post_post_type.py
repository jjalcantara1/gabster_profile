# Generated by Django 3.2.8 on 2023-10-13 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_remove_post_post_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('picture', 'Picture'), ('video', 'Video')], default='picture', max_length=20),
        ),
    ]
