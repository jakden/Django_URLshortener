# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minihtml', '0006_auto_20151213_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.URLField(unique=True, max_length=2000),
        ),
    ]
