# Generated by Django 4.0.3 on 2022-04-03 15:55

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
            name='Student',
            fields=[
                ('matric_no', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('staff_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(default=None, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]