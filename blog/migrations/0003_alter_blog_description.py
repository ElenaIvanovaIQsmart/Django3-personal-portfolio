# Generated by Django 4.2 on 2023-05-03 12:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]