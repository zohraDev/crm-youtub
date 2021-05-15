# Generated by Django 3.2.2 on 2021-05-06 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
        ('client', '0001_initial'),
        ('commande', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client'),
        ),
        migrations.AddField(
            model_name='commande',
            name='produit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.produit'),
        ),
    ]
