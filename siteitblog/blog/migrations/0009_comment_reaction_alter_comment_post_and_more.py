# Generated by Django 4.2.11 on 2024-04-18 08:57

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_options_remove_post_comments_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reaction',
            field=models.JSONField(blank=True, default=blog.models.get_default_reaction, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=155, verbose_name='Комментарий'),
        ),
    ]
