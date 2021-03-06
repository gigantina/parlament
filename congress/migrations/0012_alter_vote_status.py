# Generated by Django 4.0.2 on 2022-02-03 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0011_alter_vote_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Воздержался'), ('n', 'Против'), ('y', 'За')], default='m', help_text='Вариант ответа', max_length=1),
        ),
    ]
