# Generated by Django 3.0 on 2020-01-25 00:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'playing'), (1, 'won'), (2, 'lost')], default=0)),
                ('board', models.TextField(blank=True, default='')),
                ('rows', models.IntegerField(default=9)),
                ('columns', models.IntegerField(default=9)),
                ('mines', models.IntegerField(default=10)),
                ('difficulty', models.IntegerField(choices=[(0, 'easy'), (1, 'intermediate'), (2, 'hard')], default=0)),
                ('duration', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
