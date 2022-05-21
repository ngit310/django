from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddEquipment, AddPlots, AddAccounting, AddReviewing, AddUsers, AddEmployee
from .models import Equipmentdb, Plotsdb, Accountingdb, Reviewingdb, Users, employee_User
from django.views import View
from django.http import HttpResponseRedirect
import pymysql

con = pymysql.connect(host='localhost',
                      user='admin',
                      password='Qwerty777',
                      database='mainbase')

auth_key = 0
user_id = 0

users_query = "SELECT firstapp_users.id, person_Employee FROM firstapp_employee_user INNER JOIN firstapp_users ON firstapp_employee_user.users_id_id = firstapp_users.id"

res_users = []
with con.cursor() as cursor:
    cursor.execute(users_query)
    result = cursor.fetchall()

    for row in result:
        res_users.append([row[0], row[1]])

def index(request):
    global auth_key
    auth_key = 0
    return render(request, "DJApp\Template_Authorizated.html")

def auth(request):

    select_movies_query = "SELECT * FROM firstapp_users"
    global auth_key
    global user_id

    with con.cursor() as cursor:
        cursor.execute(select_movies_query)
        result = cursor.fetchall()

    if request.method == "POST":

        login_data = request.POST.get("login_in", "")
        pass_data = request.POST.get("password_in", "")

        for i in result:
            if (login_data == i[2] and pass_data == i[3]):
                user_id = i[0]
                auth_key = 1
                return HttpResponseRedirect("/main")

        auth_key = 0
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def main_menu(request):

    global user_id
    global res_users
    global auth_key

    if auth_key == 1:

        person = "Unknown person"

        for i in res_users:
            if i[0] == user_id:
                person = i[1]

        return render(request, "DJApp\Template_Main.html", {"person":person})
    else:
        auth_key = 0
        return redirect('home')



# Equipment

def index_equipment(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddEquipment()
    data = Equipmentdb.objects.all()
    return render(request, "DJApp\Template_Equipment.html", {"form":form_ex, "data_show":data, "person":person})

class view_equipment(View):

    def add_equipment(request):
        if request.method == "POST":
            new_data = Equipmentdb()
            new_data.type_Equipment = request.POST.get("type_Equipment")
            new_data.number_Equipment = request.POST.get("number_Equipment")
            new_data.name_Equipment = request.POST.get("name_Equipment")
            new_data.save()
            return HttpResponseRedirect("/main/equipment")

    def del_equipment(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Equipmentdb.objects.get(id=id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/equipment")

    def update_equipment(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Equipmentdb.objects.get(id=id_data)
            update_data.type_Equipment = request.POST.get("type_Equipment")
            update_data.number_Equipment = request.POST.get("number_Equipment")
            update_data.name_Equipment = request.POST.get("name_Equipment")
            update_data.save()
            return HttpResponseRedirect("/main/equipment")

# Plots

def index_plots(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddPlots()
    data = Plotsdb.objects.all()
    return render(request, "DJApp\Template_Plots.html", {"form":form_ex, "data_show":data, "person":person})

class view_plots(View):

    def add_plots(request):
        if request.method == "POST":
            new_data = Plotsdb()
            new_data.number_Plots = request.POST.get("number_Plots")
            new_data.name_Plots = request.POST.get("name_Plots")
            new_data.equipment_id = Equipmentdb.objects.get(id=request.POST.get("equipment_id"))
            new_data.save()
            return HttpResponseRedirect("/main/plots")

    def del_plots(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Plotsdb.objects.get(id=id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/plots")

    def update_plots(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Plotsdb.objects.get(id=id_data)
            update_data.number_Plots = request.POST.get("number_Plots")
            update_data.name_Plots = request.POST.get("name_Plots")
            update_data.equipment_id = Equipmentdb.objects.get(id=request.POST.get("equipment_id"))
            update_data.save()
            return HttpResponseRedirect("/main/plots")

# Accounting

def index_acc(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddAccounting()
    data = Accountingdb.objects.all()
    return render(request, "DJApp\Template_Accounting.html", {"form":form_ex, "data_show":data, "person":person})

class view_acc(View):

    def add_acc(request):
        if request.method == "POST":
            new_data = Accountingdb()
            new_data.date_Accounting = request.POST.get("date_Accounting")
            new_data.reason_Accounting = request.POST.get("reason_Accounting")
            new_data.equipment_id = Equipmentdb.objects.get(id=request.POST.get("equipment_id"))
            new_data.person_Accounting = request.POST.get("person_Accounting")
            new_data.save()
            return HttpResponseRedirect("/main/accounting")

    def del_acc(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Accountingdb.objects.get(id=id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/accounting")

    def update_acc(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Accountingdb.objects.get(id=id_data)
            update_data.date_Accounting = request.POST.get("date_Accounting")
            update_data.reason_Accounting = request.POST.get("reason_Accounting")
            update_data.equipment_id = Equipmentdb.objects.get(id=request.POST.get("equipment_id"))
            update_data.person_Accounting = request.POST.get("person_Accounting")
            update_data.save()
            return HttpResponseRedirect("/main/accounting")

# Reviewing

def index_review(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddReviewing()
    data = Reviewingdb.objects.all()
    return render(request, "DJApp\Template_Reviewing.html", {"form":form_ex, "data_show":data, "person":person})

class view_review(View):

    def add_review(request):
        if request.method == "POST":
            new_data = Reviewingdb()
            new_data.date_Reviewing = request.POST.get("date_Reviewing")
            new_data.result_Reviewing = request.POST.get("result_Reviewing")
            new_data.reason_Reviewing = request.POST.get("reason_Reviewing")
            new_data.equipment_id = Equipmentdb.objects.get(id=request.POST.get("equipment_id"))
            new_data.person_Reviewing = request.POST.get("person_Reviewing")
            new_data.save()
            return HttpResponseRedirect("/main/reviewing")

    def del_review(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Reviewingdb.objects.get(id=id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/reviewing")

    def update_review(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Reviewingdb.objects.get(id=id_data)
            update_data.date_Reviewing = request.POST.get("date_Reviewing")
            update_data.result_Reviewing = request.POST.get("result_Reviewing")
            update_data.reason_Reviewing = request.POST.get("reason_Reviewing")
            update_data.equipment_id = Equipmentdb.objects.get(id=request.POST.get("equipment_id"))
            update_data.person_Reviewing = request.POST.get("person_Reviewing")
            update_data.save()
            return HttpResponseRedirect("/main/reviewing")

# Users

def index_users(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddUsers()
    data = Users.objects.all()
    return render(request, "DJApp\Template_Users.html", {"form":form_ex, "data_show":data, "person":person})

class view_users(View):

    def add_users(request):
        if request.method == "POST":
            new_data = Users()
            new_data.number = request.POST.get("number")
            new_data.login = request.POST.get("login")
            new_data.password = request.POST.get("password")
            new_data.save()
            return HttpResponseRedirect("/main/users")

    def del_users(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = Users.objects.get(id=id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/users")

    def update_users(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = Users.objects.get(id=id_data)
            update_data.number = request.POST.get("number")
            update_data.login = request.POST.get("login")
            update_data.password = request.POST.get("password")
            update_data.save()
            return HttpResponseRedirect("/main/users")

# Employee

def index_employee(request):

    global user_id
    global res_users
    global auth_key

    person = "Unknown person"

    if auth_key == 0:
        return redirect('home')

    for i in res_users:
        if i[0] == user_id:
            person = i[1]

    form_ex = AddEmployee()
    data = employee_User.objects.all()
    return render(request, "DJApp\Template_Employee.html", {"form":form_ex, "data_show":data, "person":person})

class view_employee(View):

    def add_employee(request):
        if request.method == "POST":
            new_data = employee_User()
            new_data.number_Employee = request.POST.get("number_Employee")
            new_data.users_id = Users.objects.get(id=request.POST.get("users_id"))
            new_data.position_Employee = request.POST.get("position_Employee")
            new_data.person_Employee = request.POST.get("person_Employee")
            new_data.save()
            return HttpResponseRedirect("/main/employee")

    def del_employee(request):
        if request.method == "POST":
            id_data = request.POST.get("delname", "")
            del_data = employee_User.objects.get(id=id_data)
            del_data.delete()
            return HttpResponseRedirect("/main/employee")

    def update_employee(request):
        if request.method == "POST":
            id_data = request.POST.get("upname", "")
            update_data = employee_User.objects.get(id=id_data)
            update_data.number_Employee = request.POST.get("number_Employee")
            update_data.users_id = Users.objects.get(id=request.POST.get("users_id"))
            update_data.position_Employee = request.POST.get("position_Employee")
            update_data.person_Employee = request.POST.get("person_Employee")
            update_data.save()
            return HttpResponseRedirect("/main/employee")