# Generated by Django 3.0.8 on 2020-07-20 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0002_auto_20200720_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='sender_login',
            field=models.CharField(default='1', max_length=255),
            preserve_default=False,
        ),
    ]
