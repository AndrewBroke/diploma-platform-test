# Generated by Django 4.0.5 on 2023-01-20 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platformApp', '0003_simpleanswer_simplequestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='simplequestion',
            old_name='corrent_answer',
            new_name='correct_answer',
        ),
    ]
