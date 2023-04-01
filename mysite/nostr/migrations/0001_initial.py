# Generated by Django 4.1.7 on 2023-04-01 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('public_key', models.CharField(max_length=250)),
                ('private_key', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('uri', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nostr_id', models.CharField(max_length=500)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nostr.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nostr_id', models.CharField(max_length=500)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nostr.brand')),
            ],
        ),
    ]