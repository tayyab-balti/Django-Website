# Generated by Django 5.0.1 on 2024-08-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_alter_uploadedimage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processing_time', models.FloatField()),
                ('accuracy', models.FloatField()),
            ],
        ),
    ]
