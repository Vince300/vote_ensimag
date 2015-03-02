# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0009_auto_20150228_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votant',
            name='apprentis',
            field=models.BooleanField(verbose_name='Apprentis', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='votant',
            name='phelmag',
            field=models.BooleanField(verbose_name='Phelmag', default=False),
            preserve_default=True,
        ),
    ]
