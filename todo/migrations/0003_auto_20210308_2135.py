# Generated by Django 3.1.7 on 2021-03-08 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210308_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='username',
        ),
        migrations.AddField(
            model_name='todo',
            name='uname',
            field=models.CharField(default=99, max_length=30),
            preserve_default=False,
        ),
    ]