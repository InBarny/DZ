# Generated by Django 5.1.6 on 2025-02-12 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_coment_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='coment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.coment', verbose_name='Родительский комментарий'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('reaction', models.IntegerField(choices=[(1, 'Like'), (-1, 'Dislike')], verbose_name='Реакция')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Реакция',
                'verbose_name_plural': 'Реакции',
            },
        ),
        migrations.DeleteModel(
            name='lick',
        ),
    ]
