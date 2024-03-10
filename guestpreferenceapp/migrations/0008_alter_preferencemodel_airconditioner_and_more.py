# Generated by Django 4.2.9 on 2024-03-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guestpreferenceapp', '0007_alter_preferencemodel_heater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencemodel',
            name='airconditioner',
            field=models.BooleanField(choices=[('True', 'on'), ('False', 'off')], default='Boolean_choice[1]', null=True),
        ),
        migrations.AlterField(
            model_name='preferencemodel',
            name='heater',
            field=models.BooleanField(choices=[('True', 'on'), ('False', 'off')], default='Boolean_choice[1]', null=True),
        ),
    ]
