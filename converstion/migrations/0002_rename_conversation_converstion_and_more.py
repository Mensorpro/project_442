# Generated by Django 4.2.7 on 2023-11-11 20:05

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_alter_item_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('converstion', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Conversation',
            new_name='Converstion',
        ),
        migrations.AlterModelOptions(
            name='converstion',
            options={'ordering': ('-modified',)},
        ),
        migrations.AlterModelOptions(
            name='converstionmessage',
            options={'ordering': ('-time',)},
        ),
    ]