# Generated by Django 4.0 on 2022-03-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.CharField(max_length=1000)),
                ('user2', models.CharField(max_length=1000)),
                ('text', models.TextField()),
            ],
        ),
    ]
