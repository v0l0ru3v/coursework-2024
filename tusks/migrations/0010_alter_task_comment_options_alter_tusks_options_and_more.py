# Generated by Django 4.2.2 on 2023-06-29 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tusks', '0009_alter_task_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task_comment',
            options={'verbose_name': ('Комментарии к задачам',), 'verbose_name_plural': 'Комментарии к задачам'},
        ),
        migrations.AlterModelOptions(
            name='tusks',
            options={'verbose_name': ('Задача',), 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterModelOptions(
            name='user_tusks',
            options={'verbose_name': ('Пользователи и задачи',), 'verbose_name_plural': 'Пользователи и задачи'},
        ),
        migrations.CreateModel(
            name='Complited',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complite_date', models.DateTimeField(auto_now_add=True)),
                ('tusks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tusks.tusks')),
            ],
        ),
    ]