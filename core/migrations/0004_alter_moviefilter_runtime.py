# Generated by Django 4.1.5 on 2023-03-10 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_moviefilter_overview_moviefilter_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviefilter',
            name='runtime',
            field=models.IntegerField(default=0),
        ),
    ]
