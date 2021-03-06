# Generated by Django 3.0.4 on 2020-09-09 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180328_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_author', models.CharField(max_length=50, verbose_name='İsim')),
                ('rating_content', models.CharField(max_length=1, verbose_name='Degerlendirme')),
                ('rating_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to='article.Article', verbose_name='Makale')),
            ],
        ),
    ]
