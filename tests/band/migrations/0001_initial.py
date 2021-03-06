# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 13:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bitemporal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_valid_start_date', models.DateTimeField()),
                ('_valid_end_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('_txn_start_date', models.DateTimeField(auto_now_add=True)),
                ('_txn_end_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('name', models.CharField(max_length=128)),
                ('_master', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bitemporal.MasterObject')),
            ],
            options={
                'abstract': False,
                'ordering': ('_valid_start_date',),
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_valid_start_date', models.DateTimeField()),
                ('_valid_end_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('_txn_start_date', models.DateTimeField(auto_now_add=True)),
                ('_txn_end_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('date_joined', models.DateField()),
                ('_master', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bitemporal.MasterObject')),
            ],
            options={
                'abstract': False,
                'ordering': ('_valid_start_date',),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_valid_start_date', models.DateTimeField()),
                ('_valid_end_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('_txn_start_date', models.DateTimeField(auto_now_add=True)),
                ('_txn_end_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999, tzinfo=utc))),
                ('name', models.CharField(max_length=128)),
                ('_master', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='bitemporal.MasterObject')),
            ],
            options={
                'abstract': False,
                'ordering': ('_valid_start_date',),
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='band.Band'),
        ),
        migrations.AddField(
            model_name='band',
            name='members',
            field=models.ManyToManyField(through='band.Membership', to='band.Person'),
        ),
        migrations.AlterIndexTogether(
            name='person',
            index_together=set([('id', '_valid_start_date', '_valid_end_date', '_txn_end_date')]),
        ),
        migrations.AlterIndexTogether(
            name='membership',
            index_together=set([('id', '_valid_start_date', '_valid_end_date', '_txn_end_date')]),
        ),
        migrations.AlterIndexTogether(
            name='band',
            index_together=set([('id', '_valid_start_date', '_valid_end_date', '_txn_end_date')]),
        ),
    ]
