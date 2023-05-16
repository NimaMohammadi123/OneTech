# Generated by Django 4.0.1 on 2023-05-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Published', 'published'), ('Draft', 'draft')], default='published', max_length=50),
        ),
    ]
