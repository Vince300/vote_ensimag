# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_liste_nombre_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liste',
            name='liste_couleur',
            field=models.CharField(verbose_name='Couleur (hexa)', max_length=7, default='#fff'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liste',
            name='liste_logo',
            field=models.ImageField(upload_to='logos_listes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liste',
            name='liste_nom',
            field=models.CharField(verbose_name='Nom', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liste',
            name='nombre_votes',
            field=models.IntegerField(verbose_name='Nombre de votes', default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='liste',
            name='type',
            field=models.ForeignKey(verbose_name='Type de liste', to='votes.TypeListe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='typeliste',
            name='typeliste_nom',
            field=models.CharField(verbose_name='Nom du type', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='date',
            field=models.DateTimeField(verbose_name='Date et heure'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='ip',
            field=models.IPAddressField(verbose_name='Adresse IP'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='liste',
            field=models.ForeignKey(verbose_name='Liste', to='votes.Liste'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vote',
            name='pseudo',
            field=models.CharField(verbose_name='Pseudo du voteur', max_length=50),
            preserve_default=True,
        ),
    ]
