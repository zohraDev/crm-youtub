# Generated by Django 3.2.2 on 2021-05-06 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0005_rename_stuts_commande_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='date_created',
            new_name='created_at',
        ),
    ]