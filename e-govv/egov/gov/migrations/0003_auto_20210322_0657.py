# Generated by Django 3.1.7 on 2021-03-22 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov', '0002_auto_20210303_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='expiry_date',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='issue_date',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]