# Generated by Django 4.1.7 on 2023-05-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbeng', '0014_remove_course_description_course_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='course_name',
            field=models.CharField(default='Не выбран курс', max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('visa', 'Visa'), ('mastercard', 'MasterCard'), ('paypal', 'PayPal'), ('elcard', 'Элькарт')], default='Не выбран метод', max_length=50, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_amount',
            field=models.FloatField(default=0, verbose_name='Сумма платежа'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата оплаты'),
        ),
    ]
