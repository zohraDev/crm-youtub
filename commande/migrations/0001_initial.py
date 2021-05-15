# Generated by Django 3.2.2 on 2021-05-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuts', models.CharField(choices=[('en instance', 'en instance'), ('non livré', 'non livré'), ('livré', 'livré')], max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
