# Generated by Django 3.1.5 on 2021-01-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0002_auto_20210106_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
