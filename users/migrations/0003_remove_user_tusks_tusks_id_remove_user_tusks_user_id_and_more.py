# Generated by Django 4.2.2 on 2023-06-28 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_tusks_user_tusks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_tusks',
            name='tusks_id',
        ),
        migrations.RemoveField(
            model_name='user_tusks',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Tusks',
        ),
        migrations.DeleteModel(
            name='User_Tusks',
        ),
    ]
