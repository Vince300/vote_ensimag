# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0004_auto_20150227_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='est_second_tour',
            field=models.BooleanField(default=False, verbose_name='Second tour ?'),
            preserve_default=True,
        ),
    ]
