# Generated by Django 4.0.2 on 2022-02-01 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_congressman',
            field=models.BooleanField(default=False),
        ),
    ]
