# Generated by Django 5.1 on 2024-08-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='budget',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
