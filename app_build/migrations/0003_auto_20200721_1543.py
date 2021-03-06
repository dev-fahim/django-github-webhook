# Generated by Django 3.0.8 on 2020-07-21 09:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app_build', '0002_auto_20200721_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='appbuildrecord',
            name='build_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Build local ID'),
        ),
        migrations.AddField(
            model_name='appbuildrecord',
            name='event_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Event local ID'),
        ),
    ]
