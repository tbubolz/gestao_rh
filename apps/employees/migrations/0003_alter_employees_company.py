# Generated by Django 4.2.1 on 2023-06-14 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('employees', '0002_employees_company_employees_departments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='company.company'),
        ),
    ]
