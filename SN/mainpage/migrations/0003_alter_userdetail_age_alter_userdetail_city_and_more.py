# Generated by Django 4.0 on 2022-02-19 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_photo_userdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.photo'),
        ),
    ]