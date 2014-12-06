# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diner',
            fields=[
                ('did', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('loc', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DinerHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=2, choices=[(b'MO', b'Monday'), (b'TU', b'Tuesday'), (b'WE', b'Wednesday'), (b'TH', b'Thursday'), (b'FR', b'Friday'), (b'SA', b'Saturday'), (b'SU', b'Sunday')])),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
                ('did', models.ForeignKey(to='express.Diner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Include',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('iid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('timeToCook', models.TimeField()),
                ('did', models.ForeignKey(to='express.Diner')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ItemHour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=2, choices=[(b'MO', b'Monday'), (b'TU', b'Tuesday'), (b'WE', b'Wednesday'), (b'TH', b'Thursday'), (b'FR', b'Friday'), (b'SA', b'Saturday'), (b'SU', b'Sunday')])),
                ('openTime', models.TimeField()),
                ('closeTime', models.TimeField()),
                ('iid', models.ForeignKey(to='express.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oid', models.AutoField(serialize=False, primary_key=True)),
                ('timePlaced', models.DateTimeField()),
                ('scheduledPickUpTime', models.DateTimeField()),
                ('stat', models.CharField(default=b'PE', max_length=2, choices=[(b'PE', b'Pending'), (b'AC', b'Accepted'), (b'RE', b'Ready'), (b'PI', b'Picked')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('cardid', models.PositiveIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='cardid',
            field=models.ForeignKey(to='express.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='did',
            field=models.ForeignKey(to='express.Diner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='include',
            name='iid',
            field=models.ForeignKey(to='express.Item'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='include',
            name='oid',
            field=models.ForeignKey(to='express.Order'),
            preserve_default=True,
        ),
    ]
