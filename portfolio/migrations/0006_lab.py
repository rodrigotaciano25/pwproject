# Generated by Django 4.2.2 on 2023-06-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_cadeira_link_cadeira'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descricao', models.TextField(max_length=1000)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
    ]