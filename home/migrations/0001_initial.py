# Generated by Django 5.1.6 on 2025-03-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='carousel_images/')),
                ('link', models.URLField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
