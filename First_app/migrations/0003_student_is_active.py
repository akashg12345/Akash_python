# Generated by Django 4.0.1 on 2022-01-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_app', '0002_alter_student_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
