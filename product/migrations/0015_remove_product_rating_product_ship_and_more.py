# Generated by Django 5.0.6 on 2024-05-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_rating_alter_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.AddField(
            model_name='product',
            name='ship',
            field=models.CharField(choices=[('Surigao City', 'Surigao City'), ('China', 'China'), ('Luzon', 'Luzon'), ('Bayot City', 'Bayot City'), ('Visayas', 'Visayas')], default='1', max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Liptint', 'Liptint'), ('Foundations', 'Foundations')], default='crochets', max_length=25),
        ),
    ]
