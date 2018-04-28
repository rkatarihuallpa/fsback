# Generated by Django 2.0.4 on 2018-04-28 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.DateField(verbose_name='fecha de publicacion')),
            ],
        ),
        migrations.CreateModel(
            name='QueHacer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(max_length=300)),
                ('realizado', models.BooleanField(default=False)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='que_hacer.Grupo')),
            ],
        ),
    ]
