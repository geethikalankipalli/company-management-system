from django import forms
from .models import Employee, Project, Task, Department


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'name',
            'email',
            'phone',
            'job_title',
            'department',
            'salary',
            'joining_date',
        ]

        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Enter 10-digit phone number',
                    'maxlength': '10',
                    'inputmode': 'numeric',
                    'pattern': '[0-9]{10}',
                }
            ),
            'joining_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'description',
            'start_date',
            'end_date',
            'status',
        ]

        widgets = {
            'start_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'end_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'project',
            'title',
            'description',
            'status',
            'due_date',
        ]

        widgets = {
            'due_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name',
            'description',
        ]