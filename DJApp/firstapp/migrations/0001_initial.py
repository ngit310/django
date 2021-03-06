# Generated by Django 4.0.5 on 2022-06-03 09:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_Employee', models.IntegerField()),
                ('position_Employee', models.CharField(max_length=120)),
                ('person_Employee', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Equipmentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_Equipment', models.CharField(blank=True, max_length=120)),
                ('number_Equipment', models.IntegerField()),
                ('name_Equipment', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('login', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Reviewing', models.DateField(default=datetime.date.today)),
                ('result_Reviewing', models.CharField(max_length=120)),
                ('reason_Reviewing', models.CharField(max_length=120)),
                ('person_Reviewing', models.CharField(max_length=120)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.equipmentdb')),
            ],
        ),
        migrations.CreateModel(
            name='Plotsdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_Plots', models.IntegerField()),
                ('name_Plots', models.CharField(max_length=120)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.equipmentdb')),
            ],
        ),
        migrations.CreateModel(
            name='Accountingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_Accounting', models.DateField(default=datetime.date.today)),
                ('reason_Accounting', models.CharField(max_length=120)),
                ('person_Accounting', models.CharField(max_length=120)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.equipmentdb')),
            ],
        ),
    ]
