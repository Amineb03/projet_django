# Generated by Django 4.0.3 on 2022-05-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerapp', '0003_alter_personnel_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='utilisateur',
            fields=[
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]