# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0011_auto_20150228_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='votant',
            field=models.ForeignKey(null=True, verbose_name='Votant', to='votes.Votant'),
            preserve_default=True,
        ),
    ]
