# Generated by Django 4.2.7 on 2023-12-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=60)),
                ('body', models.TextField(max_length=300)),
            ],
        ),
    ]
