# Generated by Django 3.0.6 on 2020-05-31 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0010_auto_20200531_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='scannedhost',
            name='http_header_path',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='scannedhost',
            name='screenshot_path',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
