# Generated by Django 2.0.3 on 2018-04-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180405_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userName',
            field=models.CharField(max_length=200),
        ),
    ]