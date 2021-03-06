# Generated by Django 3.0.7 on 2020-06-24 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comments',
            field=models.TextField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rating',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
