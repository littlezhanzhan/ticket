# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('telnumber', models.CharField(max_length=11, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkSheet',
            fields=[
                ('sheet_number', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('client_type', models.IntegerField()),
                ('sheet_type', models.IntegerField()),
                ('time', models.DateField()),
                ('content', models.TextField()),
                ('method', models.TextField()),
                ('user', models.ForeignKey(to='worksheet.User')),
            ],
        ),
    ]
