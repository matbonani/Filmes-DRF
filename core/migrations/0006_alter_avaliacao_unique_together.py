# Generated by Django 3.2 on 2022-03-02 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_avaliacao_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='avaliacao',
            unique_together={('username', 'filme')},
        ),
    ]
