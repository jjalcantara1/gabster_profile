# Generated by Django 4.2.4 on 2023-10-12 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('post_type', models.CharField(choices=[('picture', 'Picture'), ('video', 'Video')], max_length=20)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
