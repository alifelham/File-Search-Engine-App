# Generated by Django 3.2.9 on 2021-12-14 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_engine', '0006_alter_crawlingqueue_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawlingqueue',
            name='depth',
            field=models.IntegerField(),
        ),
    ]
