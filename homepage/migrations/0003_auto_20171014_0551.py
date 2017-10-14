# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_user_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aboutMe',
            field=models.TextField(default='I did not write an about me'),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default='Mars', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullName',
            field=models.CharField(default='craig', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='male', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='interestTree',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='user',
            name='orientation',
            field=models.CharField(default='straight', max_length=16),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.CharField(default='foo', max_length=16),
        ),
    ]
