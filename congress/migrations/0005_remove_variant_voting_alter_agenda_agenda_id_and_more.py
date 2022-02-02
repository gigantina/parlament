# Generated by Django 4.0.2 on 2022-02-02 01:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('congress', '0004_claim_title_variant_title_voting_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='voting',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='agenda_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='claim',
            name='claim_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meet_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='variant',
            name='variant_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='voting',
            name='voting_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='VariantsVoting',
            fields=[
                ('varvot_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='congress.variant')),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='congress.voting')),
            ],
        ),
    ]