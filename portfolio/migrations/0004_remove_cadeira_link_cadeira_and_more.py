# Generated by Django 4.2.2 on 2023-06-15 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_cadeira_ranking_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadeira',
            name='link_cadeira',
        ),
        migrations.RemoveField(
            model_name='cadeira',
            name='linguagens',
        ),
        migrations.DeleteModel(
            name='Tecnologia',
        ),
        migrations.AddField(
            model_name='cadeira',
            name='linguagens',
            field=models.CharField(default='1', max_length=40),
        ),
    ]
