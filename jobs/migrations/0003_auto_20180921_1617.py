# Generated by Django 2.1.1 on 2018-09-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20180921_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='featured',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='highlight_job',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='logo',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
