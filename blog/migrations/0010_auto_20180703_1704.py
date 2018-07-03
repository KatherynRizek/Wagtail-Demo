# Generated by Django 2.0.7 on 2018-07-03 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('blog', '0009_blogpage_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogpagegalleryimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='blogpagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogtagindexpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogCategory',
        ),
        migrations.DeleteModel(
            name='BlogPage',
        ),
        migrations.DeleteModel(
            name='BlogPageGalleryImage',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.DeleteModel(
            name='BlogTagIndexPage',
        ),
    ]