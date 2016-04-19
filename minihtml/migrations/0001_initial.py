# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('website', models.URLField(max_length=2000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tiny', models.CharField(max_length=2000)),
            ],
        ),
    ]
