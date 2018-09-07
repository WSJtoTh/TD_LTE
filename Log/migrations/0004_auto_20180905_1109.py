# Generated by Django 2.1.1 on 2018-09-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0003_auto_20180905_1106'),
    ]

    operations = [

        migrations.AddField(
            model_name='test2',
            name='password',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test2',
            name='state',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test2',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test2',
            name='username',
            field=models.CharField(default=0, max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='test2',
            table='user',
        ),
        migrations.AlterModelTable(
            name='userlist',
            table='userlist',
        ),
    ]
