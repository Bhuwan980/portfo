# Generated by Django 4.0.1 on 2022-01-26 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
