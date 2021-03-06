# Generated by Django 2.0.3 on 2018-04-05 04:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_post_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='userName',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publish Date'),
        ),
    ]
