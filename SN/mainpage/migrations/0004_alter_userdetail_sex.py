# Generated by Django 4.0 on 2022-02-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_alter_userdetail_age_alter_userdetail_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='sex',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('None', 'None')], default=('None', 'None'), max_length=10),
        ),
    ]
