# Generated by Django 4.1.7 on 2023-04-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbeng', '0005_alter_grade_assessment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
