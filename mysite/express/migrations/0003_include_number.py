# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('express', '0002_auto_20141110_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='include',
            name='number',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
