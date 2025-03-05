# Generated by Django 5.1.6 on 2025-03-05 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bookdonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookExchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=255)),
                ('email_or_phone', models.CharField(max_length=100)),
                ('book_title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(choices=[('fiction', 'Fiction'), ('non_fiction', 'Non-Fiction'), ('education', 'Educational'), ('biography', 'Biography'), ('fantasy', 'Fantasy'), ('history', 'History'), ('mystery', 'Mystery'), ('science', 'Science')], max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('delivery_option', models.CharField(choices=[('drop_off', 'Drop off at location'), ('personal_pickup', 'Personal pick-up')], max_length=20)),
                ('book_image', models.ImageField(upload_to='exchange_books/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.BooleanField(default=False)),
            ],
        ),
    ]
