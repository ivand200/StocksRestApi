# Generated by Django 3.2.9 on 2021-11-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0007_alter_index_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]