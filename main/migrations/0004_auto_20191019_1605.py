# Generated by Django 2.2.3 on 2019-10-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191019_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='questiona',
            field=models.CharField(max_length=200),
        ),
    ]
