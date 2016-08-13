# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20160813_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='slug',
        ),
    ]
