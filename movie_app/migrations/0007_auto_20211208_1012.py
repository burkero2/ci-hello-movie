# Generated by Django 3.2 on 2021-12-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_rename_date_item_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AddField(
            model_name='item',
            name='genre',
            field=models.CharField(default='Comedy', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='summary',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
