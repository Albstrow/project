# Generated by Django 4.1.5 on 2023-02-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('others', 'others')], max_length=6),
        ),
    ]
