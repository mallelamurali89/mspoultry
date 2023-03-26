# Generated by Django 4.1.5 on 2023-03-19 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_delete_expenses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('exp_type', models.CharField(choices=[('products', 'Products'), ('hatching', 'Hatching'), ('traveling', 'Traveling'), ('chick_feed', 'Chick Feed'), ('grower_feed', 'Grower Feed'), ('layer_feed', 'Layer Feed'), ('medicines', 'Medicines'), ('workers', 'Workers'), ('rent', 'Rent'), ('others', 'Others')], default='others', max_length=15)),
                ('exp_description', models.TextField(blank=True, null=True)),
                ('exp_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('exp_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='relatedUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-exp_created',),
            },
        ),
    ]
