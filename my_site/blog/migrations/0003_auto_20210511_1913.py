# Generated by Django 3.2 on 2021-05-11 23:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210511_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='F', max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='school',
            name='address',
        ),
        migrations.RemoveField(
            model_name='school',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_resumption',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='fullname',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='grad_year',
            field=models.DateField(default=datetime.datetime(2021, 5, 11, 19, 12, 20, 404694)),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='certificate_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='blog.certificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='blog.grade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.department'),
        ),
    ]
