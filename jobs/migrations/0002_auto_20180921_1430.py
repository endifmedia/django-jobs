# Generated by Django 2.1.1 on 2018-09-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='category',
            field=models.CharField(max_length=380),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='instructions',
            field=models.TextField(),
        ),
    ]
