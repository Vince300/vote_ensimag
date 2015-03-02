# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_auto_20150226_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='liste',
            name='est_vote_blanc',
            field=models.BooleanField(default=False, verbose_name='Vote blanc'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liste',
            name='liste_logo',
            field=models.ImageField(upload_to='logos', blank=True, verbose_name='Logo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='pseudo',
            field=models.CharField(max_length=50, verbose_name='Pseudo du votantls'),
            preserve_default=True,
        ),
    ]
