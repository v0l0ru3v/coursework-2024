# Generated by Django 4.2.2 on 2023-06-28 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tusks', '0008_alter_task_comment_options_alter_user_tusks_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task_comment',
            options={'verbose_name': ('Task Comment',), 'verbose_name_plural': 'Task Comments'},
        ),
    ]
