# Generated by Django 4.0.3 on 2022-03-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_changed_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='changed_at',
        ),
    ]