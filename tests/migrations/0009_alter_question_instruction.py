# Generated by Django 4.0.3 on 2022-04-09 00:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_question_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='instruction',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
