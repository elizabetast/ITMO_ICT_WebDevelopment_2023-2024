# Generated by Django 3.2.10 on 2023-11-28 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorregistration',
            name='presentation_title',
            field=models.CharField(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='authorregistration',
            name='date_registered',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
