# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20150227_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='liste',
            name='nombre_votes',
        ),
        migrations.AddField(
            model_name='liste',
            name='nombre_votes_1',
            field=models.IntegerField(verbose_name='# votes tour 1', default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='liste',
            name='nombre_votes_2',
            field=models.IntegerField(verbose_name='# votes tour 2', default=0, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liste',
            name='liste_couleur',
            field=models.CharField(verbose_name='Couleur (hexa)', default='#000', max_length=7),
            preserve_default=True,
        ),
    ]
