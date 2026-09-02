from django.urls import path
from . import views

urlpatterns = [
    
    # Employees
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employees, name='employees'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    
    # Projects
    path('projects/', views.projects, name='projects'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/edit/<int:project_id>/', views.edit_Project, name='edit_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    
    
    # Tasks
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),    
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    path('departments/', views.departments, name='departments'),
    path('departments/add/', views.add_department, name='add_department'),
    path('departments/edit/<int:department_id>/', views.edit_department, name='edit_department'),
    path('departments/delete/<int:department_id>/', views.delete_department, name='delete_department'),
    
    #Reports
    path('reports/', views.reports, name='reports'),
]

