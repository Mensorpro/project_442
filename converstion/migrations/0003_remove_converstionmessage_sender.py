# Generated by Django 4.2.7 on 2023-11-11 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converstion', '0002_rename_conversation_converstion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='converstionmessage',
            name='sender',
        ),
    ]
