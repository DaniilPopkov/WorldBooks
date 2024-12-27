# Generated by Django 4.2 on 2024-12-27 11:21

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_image_alter_person_age_alter_person_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='audios', verbose_name='Аудио файл')),
            ],
            managers=[
                ('obj_audio', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='files', verbose_name='Файл PDF')),
            ],
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Видео файл')),
            ],
            managers=[
                ('obj_video', django.db.models.manager.Manager()),
            ],
        ),
    ]