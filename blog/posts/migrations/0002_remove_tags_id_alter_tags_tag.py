# Generated by Django 5.0.4 on 2024-04-27 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tags',
            name='id',
        ),
        migrations.AlterField(
            model_name='tags',
            name='Tag',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
