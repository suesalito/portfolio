# Generated by Django 2.2.10 on 2020-03-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='nickname',
            field=models.CharField(default='', max_length=200),
        ),
    ]
