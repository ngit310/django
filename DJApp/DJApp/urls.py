from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [

    # Начальные страницы
    path('', views.index, name='home'),
    path('loging/', views.auth, name='loging'),
    path('main/', views.main_menu, name='main'),

    # Equipment
    path('main/equipment/', views.index_equipment, name='equipment'),
    path('main/equipment/add_equipment/', views.view_equipment.add_equipment, name='add_equipment'),
    path('main/equipment/del_equipment/', views.view_equipment.del_equipment, name='del_equipment'),
    path('main/equipment/update_equipment/', views.view_equipment.update_equipment, name='update_equipment'),

    # Plots
    path('main/plots/', views.index_plots, name='plots'),
    path('main/plots/add_plots/', views.view_plots.add_plots, name='add_plots'),
    path('main/plots/del_plots/', views.view_plots.del_plots, name='del_plots'),
    path('main/plots/update_plots/', views.view_plots.update_plots, name='update_plots'),

    # Accounting
    path('main/accounting/', views.index_acc, name='accounting'),
    path('main/accounting/add_accounting/', views.view_acc.add_acc, name='add_accounting'),
    path('main/accounting/del_accounting/', views.view_acc.del_acc, name='del_accounting'),
    path('main/accounting/update_accounting/', views.view_acc.update_acc, name='update_accounting'),

    # Reviewing
    path('main/reviewing/', views.index_review, name='reviewing'),
    path('main/reviewing/add_reviewing/', views.view_review.add_review, name='add_reviewing'),
    path('main/reviewing/del_reviewing/', views.view_review.del_review, name='del_reviewing'),
    path('main/reviewing/update_reviewing/', views.view_review.update_review, name='update_reviewing'),

    # Users
    path('main/users/', views.index_users, name='users'),
    path('main/users/add_users/', views.view_users.add_users, name='add_users'),
    path('main/users/del_users/', views.view_users.del_users, name='del_users'),
    path('main/users/update_users/', views.view_users.update_users, name='update_users'),

    # Employee
    path('main/employee/', views.index_employee, name='employee'),
    path('main/employee/add_employee/', views.view_employee.add_employee, name='add_employee'),
    path('main/employee/del_employee/', views.view_employee.del_employee, name='del_employee'),
    path('main/employee/update_employee/', views.view_employee.update_employee, name='update_employee'),

]
