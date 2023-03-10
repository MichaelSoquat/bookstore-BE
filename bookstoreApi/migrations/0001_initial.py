# Generated by Django 4.1.5 on 2023-01-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('buyed_at', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('is_read', models.BooleanField()),
                ('rating', models.IntegerField()),
                ('notice', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
