# Generated by Django 3.2.8 on 2021-12-01 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0015_signigreq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signigreq',
            name='doc_url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signer', to='documents.reqsigndoc'),
        ),
        migrations.AlterField(
            model_name='signigreq',
            name='signed_url',
            field=models.CharField(max_length=225),
        ),
    ]
