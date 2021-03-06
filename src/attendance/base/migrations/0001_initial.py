# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('matriculation', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Student'),
        ),
    ]
