# Generated by Django 2.2.7 on 2020-08-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
                ('created', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
