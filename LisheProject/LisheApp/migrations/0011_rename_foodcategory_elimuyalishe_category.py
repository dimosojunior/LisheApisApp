# Generated by Django 4.1.3 on 2023-08-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LisheApp', '0010_alter_dayfive_dayname_alter_dayfour_dayname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elimuyalishe',
            old_name='FoodCategory',
            new_name='Category',
        ),
    ]
