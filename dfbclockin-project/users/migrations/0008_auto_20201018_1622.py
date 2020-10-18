# Generated by Django 3.1.2 on 2020-10-18 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('admin', 'Admin'), ('finance', 'Finance'), ('program', 'Program'), ('m&e', 'M&E'), ('communications', 'Communications'), ('it', 'IT')], max_length=20),
        ),
    ]
