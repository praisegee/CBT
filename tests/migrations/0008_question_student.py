# Generated by Django 4.0.3 on 2022-04-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0005_alter_lecturer_image_alter_student_image'),
        ('tests', '0007_remove_notification_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='student',
            field=models.ManyToManyField(to='roles.student'),
        ),
    ]