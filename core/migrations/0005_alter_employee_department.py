from django.db import migrations, models
import django.db.models.deletion


def convert_departments(apps, schema_editor):
    Employee = apps.get_model('core', 'Employee')
    Department = apps.get_model('core', 'Department')

    for employee in Employee.objects.all():
        old_department = employee.department

        if old_department and old_department.lower() == 'it':
            department = Department.objects.get(name='IT')

        elif old_department and old_department.lower() == 'analytics':
            department = Department.objects.get(name='Analytics')

        else:
            department = None

        employee.department_new = department
        employee.save(update_fields=['department_new'])


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department_new',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='core.department',
            ),
        ),

        migrations.RunPython(convert_departments),

        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),

        migrations.RenameField(
            model_name='employee',
            old_name='department_new',
            new_name='department',
        ),
    ]