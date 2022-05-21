from django import forms
from .models import Equipmentdb, Plotsdb, Accountingdb, Reviewingdb, Users, employee_User

class AddEquipment(forms.Form):
    type_Equipment = forms.CharField(label="Тип оборудования")
    number_Equipment = forms.CharField(label="Номер оборудования")
    name_Equipment = forms.CharField(label="Название оборудования")

class AddPlots(forms.Form):
    number_Plots = forms.CharField(label="Номер участка")
    name_Plots = forms.CharField(label="Название участка")
    equipment_id = forms.ModelChoiceField(label="Оборудование", queryset=Equipmentdb.objects.all().order_by('id'))

class AddAccounting(forms.Form):
    date_Accounting = forms.DateField(label="Дата отказа оборудования")
    reason_Accounting = forms.CharField(label="Причина осмотра оборудования")
    equipment_id = forms.ModelChoiceField(label="Оборудование", queryset=Equipmentdb.objects.all().order_by('id'))
    person_Accounting = forms.CharField(label="ФИО сотрудника")

class AddReviewing(forms.Form):
    date_Reviewing = forms.DateField(label="Дата технического осмотра")
    result_Reviewing = forms.CharField(label="Результат осмотра")
    reason_Reviewing = forms.CharField(label="Причина осмотра")
    equipment_id = forms.ModelChoiceField(label="Оборудование", queryset=Equipmentdb.objects.all().order_by('id'))
    person_Reviewing = forms.CharField(label="ФИО сотрудника")

class AddUsers(forms.Form):
    number = forms.IntegerField(label="Номер пользователя")
    login = forms.CharField(label="Логин пользователя")
    password = forms.CharField(label="Пароль пользователя")

class AddEmployee(forms.Form):
    number_Employee = forms.CharField(label="Номер сотрудника")
    users_id = forms.ModelChoiceField(label="Пользователь", queryset=Users.objects.all().order_by('id'))
    position_Employee = forms.CharField(label="Должность сотрудника")
    person_Employee = forms.CharField(label="ФИО сотрудника")