# Generated by Django 4.1.6 on 2023-06-09 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_remove_article_ordered_date_box_ordered_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Picture',
            new_name='portrait',
        ),
    ]