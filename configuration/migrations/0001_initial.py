# Generated by Django 4.0.2 on 2022-02-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectionTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.TimeField(unique=True)),
                ('end', models.TimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(default='', max_length=50, unique=True)),
            ],
        ),
    ]