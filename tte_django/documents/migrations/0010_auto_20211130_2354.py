# Generated by Django 3.2.8 on 2021-11-30 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0009_alter_selfsigneddoc_originaldoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfSignedDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=225)),
                ('size', models.IntegerField()),
                ('status', models.CharField(max_length=225)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('file_url', models.URLField()),
                ('signed_url', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='selfSignedDoc',
        ),
    ]
