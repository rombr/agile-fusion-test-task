# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('is_ready', models.BooleanField(default=True, db_index=True, verbose_name='Ready for work')),
            ],
            options={
                'ordering': ('-is_ready',),
                'verbose_name': 'Driver',
                'verbose_name_plural': 'Drivers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.PositiveIntegerField(verbose_name='Client ID')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('time', models.DateTimeField(verbose_name='Time for start', db_index=True)),
                ('is_closed', models.BooleanField(default=False, db_index=True, verbose_name='Finished')),
            ],
            options={
                'ordering': ('-is_closed',),
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
