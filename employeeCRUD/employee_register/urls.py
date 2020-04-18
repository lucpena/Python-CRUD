from django.urls import path, include
from . import views

urlpatterns = [
    # Get and Post request for INSERT operation
    path('', views.employee_form, name="employee_insert"),

    # Get and Post request for UPDATE operation
    path('<int:id>/', views.employee_form, name="employee_update"),

    # DELETE
    path('delete/<int:id>/', views.employee_delete, name="employee_delete"),

    # Get request to search and display the table
    path('list/', views.employee_list, name="employee_list")
]
