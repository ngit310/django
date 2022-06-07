from django.db import models
import datetime

# оборудование
class Equipmentdb(models.Model):
    type_Equipment = models.CharField(max_length=120, blank=True)
    number_Equipment = models.IntegerField()
    name_Equipment = models.CharField(max_length=120, blank=True)
    objects = models.Manager()

# участки
class Plotsdb(models.Model):
    number_Plots = models.IntegerField()
    name_Plots = models.CharField(max_length=120)
    equipment_id = models.ForeignKey('Equipmentdb', on_delete=models.CASCADE)
    objects = models.Manager()

# учёт отказа оборудования
class Accountingdb(models.Model):
    date_Accounting = models.DateField(default=datetime.date.today)
    reason_Accounting = models.CharField(max_length=120)
    equipment_id = models.ForeignKey('Equipmentdb', on_delete=models.CASCADE)
    person_Accounting = models.CharField(max_length=120)
    objects = models.Manager()

# учёт технического осмотра
class Reviewingdb(models.Model):
    date_Reviewing = models.DateField(default=datetime.date.today)
    result_Reviewing = models.CharField(max_length=120)
    reason_Reviewing = models.CharField(max_length=120)
    equipment_id = models.ForeignKey('Equipmentdb', on_delete=models.CASCADE)
    person_Reviewing = models.CharField(max_length=120)
    objects = models.Manager()

class Users(models.Model):
    number = models.IntegerField()
    login = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    objects = models.Manager()

class employee_User(models.Model):
    number_Employee = models.IntegerField()
    position_Employee = models.CharField(max_length=120)
    person_Employee = models.CharField(max_length=120)
    objects = models.Manager()