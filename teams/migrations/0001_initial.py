# Generated by Django 4.0.3 on 2022-03-11 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_section', to='configuration.section')),
                ('availability', models.ManyToManyField(to='configuration.sectiontime')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('preferred_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_section', to='configuration.section')),
            ],
        ),
    ]
