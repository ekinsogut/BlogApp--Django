# Generated by Django 3.0.4 on 2020-09-09 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['-rating_date']},
        ),
    ]
