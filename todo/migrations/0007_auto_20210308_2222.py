# Generated by Django 3.1.7 on 2021-03-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20210308_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.CharField(default='', max_length=30),
        ),
    ]