# Generated by Django 3.2.8 on 2021-12-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0020_auto_20211202_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqsigndoc',
            name='status',
            field=models.CharField(default='Pending', max_length=225),
        ),
        migrations.AlterField(
            model_name='signigreq',
            name='status',
            field=models.CharField(default='Pending', max_length=225),
        ),
    ]
