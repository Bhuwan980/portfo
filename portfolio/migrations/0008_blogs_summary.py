# Generated by Django 4.0.1 on 2022-01-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_portfolio_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
