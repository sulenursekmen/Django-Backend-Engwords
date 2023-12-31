# Generated by Django 5.0 on 2023-12-14 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=32)),
                ('mean', models.CharField(max_length=32)),
                ('sentence', models.TextField()),
                ('is_learned', models.BooleanField(default=False)),
                ('level', models.IntegerField(choices=[(1, 'A1'), (2, 'A2'), (3, 'B1'), (4, 'B2'), (5, 'C1'), (6, 'C2')], default=1)),
            ],
        ),
    ]
