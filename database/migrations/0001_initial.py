# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-19 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bo_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('bo_name', models.CharField(max_length=30)),
                ('bo_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('bo_type', models.CharField(max_length=20)),
                ('bo_publisher', models.CharField(max_length=30)),
                ('bo_author', models.CharField(max_length=20)),
                ('bo_introduce', models.TextField()),
                ('bo_ptime', models.DateField(auto_now_add=True)),
                ('bo_operator', models.CharField(max_length=20)),
                ('bo_rukutime', models.DateField(auto_now_add=True)),
                ('bo_number', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 't_book',
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateField(auto_now_add=True)),
                ('end_time', models.DateField(auto_now_add=True)),
                ('registrar', models.CharField(max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Book')),
            ],
            options={
                'db_table': 't_borrow',
            },
        ),
        migrations.CreateModel(
            name='Clazz',
            fields=[
                ('cla_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('cla_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 't_clazz',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cou_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('cou_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 't_course',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('gr_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('gr_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 't_grade',
            },
        ),
        migrations.CreateModel(
            name='HeadTeacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clazz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Clazz')),
            ],
            options={
                'db_table': 't_headTeacher',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('ma_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('ma_name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 't_major',
            },
        ),
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('st_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('st_name', models.CharField(max_length=10)),
                ('st_gender', models.CharField(max_length=10)),
                ('st_age', models.PositiveIntegerField()),
                ('st_nation', models.CharField(max_length=10)),
                ('st_political', models.CharField(max_length=10)),
                ('st_birth', models.DateField()),
                ('st_SFZ', models.CharField(max_length=20)),
                ('st_phone', models.CharField(max_length=20)),
                ('st_addr', models.TextField()),
                ('st_clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Clazz')),
            ],
            options={
                'db_table': 't_stu',
            },
        ),
        migrations.CreateModel(
            name='StuCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sc_score', models.DecimalField(decimal_places=1, max_digits=4)),
                ('sc_type', models.CharField(max_length=20)),
                ('cls', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Clazz')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Stu')),
            ],
            options={
                'db_table': 't_stuCourse',
            },
        ),
        migrations.CreateModel(
            name='StuRegister',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_score', models.PositiveIntegerField()),
                ('start_time', models.DateField()),
                ('clazz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Clazz')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Stu')),
            ],
            options={
                'db_table': 't_stuRegister',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('te_id', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('te_name', models.CharField(max_length=10)),
                ('te_gender', models.CharField(max_length=10)),
                ('te_age', models.PositiveIntegerField()),
                ('te_nation', models.CharField(max_length=10)),
                ('te_marriage', models.CharField(max_length=10)),
                ('te_political', models.CharField(max_length=10)),
                ('te_birth', models.DateField()),
                ('te_SFZ', models.PositiveIntegerField()),
                ('te_education', models.CharField(max_length=20)),
                ('te_phone', models.PositiveIntegerField()),
                ('work_content', models.TextField()),
                ('te_major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Major')),
            ],
            options={
                'db_table': 't_teacher',
            },
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rkDATE', models.DateField()),
                ('lizhiDATE', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Course')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Teacher')),
            ],
            options={
                'db_table': 't_teacherCourse',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20, unique=True)),
                ('user_pwd', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 't_user',
            },
        ),
        migrations.AddField(
            model_name='headteacher',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.Teacher'),
        ),
        migrations.AddField(
            model_name='clazz',
            name='cla_grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Grade'),
        ),
        migrations.AddField(
            model_name='clazz',
            name='cla_major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Major'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Stu'),
        ),
    ]
