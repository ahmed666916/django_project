# Generated by Django 4.2.1 on 2023-05-25 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
