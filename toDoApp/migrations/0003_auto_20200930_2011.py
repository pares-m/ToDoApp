# Generated by Django 3.1.1 on 2020-09-30 18:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0002_todolist_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]