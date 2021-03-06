# Generated by Django 4.0 on 2022-04-20 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0005_sotib_olngan_maxsulot1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotib_olngan_maxsulot2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('narx', models.IntegerField()),
                ('son', models.IntegerField(default=1)),
                ('tur', models.CharField(max_length=50)),
                ('vaqt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccessMaxsulot2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
                ('old_price', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('rasm', models.ImageField(upload_to='media')),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.accesstype')),
            ],
        ),
        migrations.CreateModel(
            name='AccessMaxsulot1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
                ('old_price', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('rasm', models.ImageField(upload_to='media')),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.accesstype')),
            ],
        ),
    ]
