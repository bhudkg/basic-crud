# Generated by Django 5.0.6 on 2024-07-13 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user_alter_contact_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
