# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20150316_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='to',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
