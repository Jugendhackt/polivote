# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151017_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.TextField(),
        ),
    ]
