# Generated by Django 4.1.13 on 2024-08-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_alter_ticket_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_state',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('In Progress', 'In Progress'), ('On Hold', 'On Hold'), ('Complete', 'Complete'), ('Rejected', 'Rejected')], default='New', max_length=30, null=True),
        ),
    ]
