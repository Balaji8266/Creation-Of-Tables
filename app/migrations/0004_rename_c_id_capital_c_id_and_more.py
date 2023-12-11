# Generated by Django 4.2.6 on 2023-12-08 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_emp_deptno_delete_dept_delete_emp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capital',
            old_name='C_id',
            new_name='c_id',
        ),
        migrations.RenameField(
            model_name='capital',
            old_name='Cap_name',
            new_name='cap_name',
        ),
        migrations.RemoveField(
            model_name='country',
            name='id',
        ),
        migrations.AlterField(
            model_name='country',
            name='C_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
