# Generated by Django 4.1.5 on 2023-02-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0013_alter_student_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
