# Generated by Django 4.0.5 on 2022-08-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
