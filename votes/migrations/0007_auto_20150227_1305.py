# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0006_typeliste_deux_tours'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='liste',
            options={'ordering': ['type', 'nom']},
        ),
        migrations.RenameField(
            model_name='liste',
            old_name='liste_nom',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='typeliste',
            old_name='typeliste_nom',
            new_name='nom',
        ),
    ]
