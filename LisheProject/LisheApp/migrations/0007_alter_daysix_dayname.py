# Generated by Django 4.1.3 on 2023-08-15 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LisheApp', '0006_alter_makundiyachakula_foodcategory_delete_vyakula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daysix',
            name='DayName',
            field=models.ForeignKey(max_length=500, on_delete=django.db.models.deletion.CASCADE, to='LisheApp.days'),
        ),
    ]