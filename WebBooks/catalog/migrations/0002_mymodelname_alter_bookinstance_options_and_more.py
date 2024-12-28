# Generated by Django 4.2 on 2024-12-28 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Не более 20 символов', max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={},
        ),
        migrations.RemoveField(
            model_name='author',
            name='date_of_death',
        ),
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(help_text='Введите сведения об авторе', null=True, verbose_name='Сведения об авторе'),
        ),
        migrations.AddField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, help_text='Введите фото автора', null=True, upload_to='images', verbose_name='Фото автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(help_text='Выберите автора (авторов) книги', to='catalog.author', verbose_name='Автор (авторы) книги'),
        ),
    ]
