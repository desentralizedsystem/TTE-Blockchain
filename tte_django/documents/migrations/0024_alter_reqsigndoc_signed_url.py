# Generated by Django 3.2.8 on 2021-12-02 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0023_alter_selfsigneddocuments_ori_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqsigndoc',
            name='signed_url',
            field=models.URLField(blank=True),
        ),
    ]
