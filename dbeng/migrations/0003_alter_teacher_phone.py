# Generated by Django 4.1.7 on 2023-04-02 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbeng', '0002_remove_teacher_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
