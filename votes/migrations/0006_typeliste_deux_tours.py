# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_vote_est_second_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeliste',
            name='deux_tours',
            field=models.BooleanField(verbose_name='Deux tours requis ?', default=False),
            preserve_default=True,
        ),
    ]
