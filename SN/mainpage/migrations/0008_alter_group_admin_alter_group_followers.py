# Generated by Django 4.0 on 2022-02-25 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_group_admin_alter_group_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='admin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainpage.userdetail'),
        ),
        migrations.AlterField(
            model_name='group',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to='mainpage.UserDetail'),
        ),
    ]