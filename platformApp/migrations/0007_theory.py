# Generated by Django 3.2.17 on 2023-05-03 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platformApp', '0006_theme_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platformApp.theme')),
            ],
        ),
    ]
