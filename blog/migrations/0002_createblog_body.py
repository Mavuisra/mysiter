# Generated by Django 4.1.2 on 2022-10-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createblog',
            name='body',
            field=models.TextField(default='boby'),
        ),
    ]
