# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0008_auto_20150227_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('prenom', models.CharField(verbose_name='Prénom', max_length=100)),
                ('nom', models.CharField(verbose_name='Nom', max_length=100)),
                ('annee', models.CharField(verbose_name='Année', max_length=2)),
                ('login', models.CharField(verbose_name='Login', max_length=8)),
                ('apprentis', models.BooleanField(verbose_name='Apprentis ?', default=False)),
                ('phelmag', models.BooleanField(verbose_name='Phelmag ?', default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='vote',
            name='pseudo',
        ),
        migrations.AddField(
            model_name='vote',
            name='votant',
            field=models.ForeignKey(verbose_name='Pseudo du votant', null=True, to='votes.Votant'),
            preserve_default=True,
        ),
    ]
