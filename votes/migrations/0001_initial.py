# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liste',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('liste_nom', models.CharField(max_length=50)),
                ('liste_logo', models.CharField(max_length=100)),
                ('liste_couleur', models.CharField(max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TypeListe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('typeliste_nom', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('pseudo', models.CharField(max_length=50)),
                ('ip', models.GenericIPAddressField()),
                ('date', models.DateTimeField()),
                ('liste', models.ForeignKey(to='votes.Liste')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='liste',
            name='type',
            field=models.ForeignKey(to='votes.TypeListe'),
            preserve_default=True,
        ),
    ]
