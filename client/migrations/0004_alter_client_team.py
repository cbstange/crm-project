# Generated by Django 5.0.2 on 2024-02-25 17:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_alter_client_options'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='team.team'),
        ),
    ]