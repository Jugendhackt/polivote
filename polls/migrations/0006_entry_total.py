# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151017_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
