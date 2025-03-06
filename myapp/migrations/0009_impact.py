# Generated by Django 5.1.6 on 2025-03-06 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_delete_bookexchange_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_impacted', models.PositiveIntegerField(default=0)),
                ('schools_reached', models.PositiveIntegerField(default=0)),
                ('exchanges_facilitated', models.PositiveIntegerField(default=0)),
                ('books_donated', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
