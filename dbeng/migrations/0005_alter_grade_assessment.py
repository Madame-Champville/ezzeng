# Generated by Django 4.1.7 on 2023-04-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbeng', '0004_alter_attendace_attendace_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='assessment',
            field=models.CharField(choices=[('2', 'poor'), ('3', 'Satisfactory'), ('4', 'good'), ('5', 'excellent')], max_length=50),
        ),
    ]