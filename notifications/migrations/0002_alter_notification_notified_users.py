# Generated by Django 5.1.5 on 2025-01-30 15:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notified_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
