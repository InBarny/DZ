# Generated by Django 5.1.6 on 2025-02-09 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_donat_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.coment', verbose_name='Родительский комментарий'),
        ),
    ]
