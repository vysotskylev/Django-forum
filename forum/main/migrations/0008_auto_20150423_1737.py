# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150423_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(to='main.Thread'),
            preserve_default=True,
        ),
    ]
