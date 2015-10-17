# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20151017_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='title',
            new_name='text',
        ),
    ]
