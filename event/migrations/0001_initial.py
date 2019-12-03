# Generated by Django 2.2.7 on 2019-12-03 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000, null=True)),
                ('photo', models.ImageField(null=True, upload_to=event.models._content_file_name)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event',
                'managed': True,
            },
        ),
    ]
