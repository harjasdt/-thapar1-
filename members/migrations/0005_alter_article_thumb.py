# Generated by Django 4.1.1 on 2022-09-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_article_delete_human'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(upload_to='models/'),
        ),
    ]
