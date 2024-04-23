# Generated by Django 4.2.11 on 2024-04-04 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.PositiveIntegerField()),
                ('is_published', models.BooleanField(choices=[(1, 'Черновик'), (2, 'Опубликовано')], default=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(default=None, max_length=1000)),
                ('img', models.CharField(max_length=255, null=True)),
                ('reaction', models.JSONField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category')),
            ],
            options={
                'ordering': ['-date_created'],
                'indexes': [models.Index(fields=['-date_created'], name='blog_post_date_cr_414575_idx')],
            },
        ),
    ]
