# Generated by Django 4.0.3 on 2022-03-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.CharField(max_length=200),
        ),
    ]
