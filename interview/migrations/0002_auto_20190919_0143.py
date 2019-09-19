# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-09-18 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='interview_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='interview_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_question_name', models.CharField(max_length=250)),
                ('interview_question_text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='interview_questions',
            name='interview_qestion_group_id',
        ),
        migrations.DeleteModel(
            name='interview_question_group',
        ),
        migrations.DeleteModel(
            name='interview_questions',
        ),
        migrations.AddField(
            model_name='interview_answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interview_question'),
        ),
    ]