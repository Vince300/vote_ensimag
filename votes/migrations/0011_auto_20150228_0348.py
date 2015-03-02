# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0010_auto_20150228_0308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='votant',
            options={'ordering': ['annee', 'nom']},
        ),
        migrations.RemoveField(
            model_name='votant',
            name='apprentis',
        ),
        migrations.AddField(
            model_name='votant',
            name='apprenti',
            field=models.BooleanField(verbose_name='Apprenti', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='est_second_tour',
            field=models.BooleanField(verbose_name='Second tour', default=False),
            preserve_default=True,
        ),
    ]
