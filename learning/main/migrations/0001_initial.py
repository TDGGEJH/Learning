# Generated by Django 4.2.9 on 2024-01-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shodki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Имя')),
                ('location', models.CharField(max_length=50, verbose_name='Локация')),
                ('desk', models.CharField(max_length=250, verbose_name='Описание')),
            ],
        ),
    ]
