# Generated by Django 2.0.7 on 2018-07-23 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('permission', '0005_auto_20180719_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perizinan',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
