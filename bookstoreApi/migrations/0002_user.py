# Generated by Django 4.1.5 on 2023-01-07 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
