# Generated by Django 3.2.2 on 2021-05-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0004_auto_20210506_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='stuts',
            new_name='status',
        ),
    ]
