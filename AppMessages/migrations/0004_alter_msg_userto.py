# Generated by Django 4.1.3 on 2023-01-18 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppMaster', '__first__'),
        ('AppMessages', '0003_alter_msg_userto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='userto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMaster.userext'),
        ),
    ]
