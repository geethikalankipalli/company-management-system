from django.contrib import admin
from .models import Employee, Project, Task, Department


admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Department)