# Generated by Django 5.2 on 2025-04-02 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libmanagement', '0002_alter_book_genre'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='booklend',
            new_name='Records',
        ),
    ]
