# Generated by Django 4.1.5 on 2023-03-19 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_expenses_exp_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='exp_date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]