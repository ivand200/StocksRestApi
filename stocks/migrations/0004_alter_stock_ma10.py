# Generated by Django 3.2.9 on 2021-11-08 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20211108_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ma10',
            field=models.FloatField(),
        ),
    ]
