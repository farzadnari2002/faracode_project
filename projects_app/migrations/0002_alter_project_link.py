# Generated by Django 4.2.7 on 2023-11-29 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.TextField(max_length=60, null=True),
        ),
    ]