# Generated by Django 4.0 on 2022-02-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0011_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='mainpage.UserDetail'),
        ),
    ]