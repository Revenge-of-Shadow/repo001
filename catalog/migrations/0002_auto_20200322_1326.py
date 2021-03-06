# Generated by Django 3.0.4 on 2020-03-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('C', 'Cancelled'), ('N', 'Not created yet'), ('X', 'Archived'), ('A', 'Available')], default='m', help_text='Game aviability:', max_length=1),
        ),
    ]
