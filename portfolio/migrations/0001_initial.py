# Generated by Django 4.0.1 on 2022-01-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='media/')),
                ('desc', models.TextField()),
            ],
        ),
    ]