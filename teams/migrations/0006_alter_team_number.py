# Generated by Django 4.0.3 on 2022-03-19 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_alter_team_member1_alter_team_member2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='number',
            field=models.SmallIntegerField(unique=True, verbose_name='Team number'),
        ),
    ]