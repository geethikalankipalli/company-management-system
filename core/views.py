from django.shortcuts import render, redirect, get_object_or_404
from.models import Employee, Project, Task, Department
from .forms import EmployeeForm, ProjectForm, TaskForm, DepartmentForm
from django.db.models import Count
from datetime import date

def dashboard(request):

    employee_count = Employee.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.count()

    pending_task_count = Task.objects.filter(
        status__iexact='pending'
    ).count()

    pending_project_count = Project.objects.filter(
        status__iexact='pending'
    ).count()

    in_progress_project_count = Project.objects.filter(
        status__iexact='in progress'
    ).count()

    completed_project_count = Project.objects.filter(
        status__iexact='completed'
    ).count()

    department_count = Department.objects.count()

    return render(request, 'dashboard.html', {
        'employee_count': employee_count,
        'project_count': project_count,
        'task_count': task_count,
        'pending_task_count': pending_task_count,
        'pending_project_count': pending_project_count,
        'in_progress_project_count': in_progress_project_count,
        'completed_project_count': completed_project_count,
        'department_count': department_count,
    })
def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

def edit_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employees')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form})

def delete_employee(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees')

    return render(request, 'delete_employee.html', {'employee': employee})




def projects(request):
    project_list = Project.objects.all()

    return render(request, 'projects.html', {
        'projects': project_list,
        'today': date.today()
    })
    
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()

    return render(request, 'add_project.html', {'form': form})

def edit_Project(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form})

def delete_project(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    return render(request, 'delete_project.html', {'project': project})




def tasks(request):
    task_list = Task.objects.all()

    return render(request, 'tasks.html',{'tasks': task_list, 'today': date.today()})
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tasks')

    else:
        form = TaskForm()

    return render(request, 'add_task.html', {
        'form': form
    })
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': form})
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

    return render(request, 'delete_task.html', {'task': task})

def departments(request):
    departments = Department.objects.annotate(
        employee_count=Count('employee')
    ).order_by('name')

    return render(request, 'department.html', {
        'departments': departments
    })
def add_department(request):

    if request.method == 'POST':

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('departments')

    else:

        form = DepartmentForm()

    return render(request, 'add_department.html', {
        'form': form
    })
    
def add_department(request):

    if request.method == 'POST':

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('departments')

    else:

        form = DepartmentForm()

    return render(request, 'add_department.html', {
        'form': form
    })


def edit_department(request, department_id):

    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':

        form = DepartmentForm(request.POST, instance=department)

        if form.is_valid():
            form.save()
            return redirect('departments')

    else:

        form = DepartmentForm(instance=department)

    return render(request, 'edit_department.html', {
        'form': form,
        'department': department
    })
def delete_department(request, department_id):

    department = get_object_or_404(Department, id=department_id)

    if request.method == 'POST':
        department.delete()
        return redirect('departments')

    return render(request, 'delete_department.html', {
        'department': department
    })



def reports(request):

    employee_count = Employee.objects.count()
    department_count = Department.objects.count()
    project_count = Project.objects.count()
    task_count = Task.objects.count()

    completed_projects = Project.objects.filter(
        status__iexact='completed'
    ).count()

    pending_projects = Project.objects.filter(
        status__iexact='pending'
    ).count()

    pending_tasks = Task.objects.filter(
        status__iexact='pending'
    ).count()

    department_data = Department.objects.annotate(
        employee_count=Count('employee')
    ).order_by('name')

    return render(request, 'reports.html', {
        'employee_count': employee_count,
        'department_count': department_count,
        'project_count': project_count,
        'task_count': task_count,
        'completed_projects': completed_projects,
        'pending_projects': pending_projects,
        'pending_tasks': pending_tasks,
        'department_data': department_data,
    })