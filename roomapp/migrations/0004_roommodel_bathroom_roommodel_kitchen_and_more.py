# Generated by Django 4.2.9 on 2024-03-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomapp', '0003_roommodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommodel',
            name='bathroom',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='kitchen',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='persons',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='roommodel',
            name='wifi',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
