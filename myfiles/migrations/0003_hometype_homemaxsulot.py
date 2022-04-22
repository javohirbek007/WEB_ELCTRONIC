# Generated by Django 4.0.3 on 2022-04-14 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_mobiletype_mobilemaxsulot'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HomeMaxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
                ('old_price', models.IntegerField()),
                ('new_price', models.IntegerField()),
                ('rasm', models.ImageField(upload_to='madia')),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.hometype')),
            ],
        ),
    ]
