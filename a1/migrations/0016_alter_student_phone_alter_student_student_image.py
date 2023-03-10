# Generated by Django 4.1.5 on 2023-02-12 02:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0015_alter_student_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
