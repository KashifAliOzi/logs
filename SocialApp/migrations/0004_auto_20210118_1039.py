# Generated by Django 3.1.5 on 2021-01-18 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialApp', '0003_auto_20210112_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.TextField(),
        ),
    ]