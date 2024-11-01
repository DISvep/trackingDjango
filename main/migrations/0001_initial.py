# Generated by Django 5.1.2 on 2024-10-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('_in_progress', 'In Progress'), ('_done', 'Done'), ('_expired', 'Expired')], max_length=12)),
                ('priority', models.CharField(choices=[('_low', 'Low'), ('_mid', 'Middle'), ('_high', 'High')], max_length=7)),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]
