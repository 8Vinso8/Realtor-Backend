# Generated by Django 4.1.4 on 2023-02-02 18:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_is_realtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='clients',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
