# Generated by Django 5.0.2 on 2024-05-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_dato_edad_alter_dato_ficha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dato',
            name='edad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dato',
            name='ficha',
            field=models.IntegerField(),
        ),
    ]