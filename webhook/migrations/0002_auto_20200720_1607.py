# Generated by Django 3.0.8 on 2020-07-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='repository_name',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webhook',
            name='repository_owner_name',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webhook',
            name='repository_url',
            field=models.URLField(default='1'),
            preserve_default=False,
        ),
    ]
