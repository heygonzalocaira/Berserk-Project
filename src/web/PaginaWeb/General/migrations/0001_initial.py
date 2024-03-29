# Generated by Django 2.1.5 on 2019-07-05 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limiteItems', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hechicero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furia', models.IntegerField(default='100')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rango', models.IntegerField(default=0)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=2)),
                ('clasificacion', models.IntegerField(default=0)),
                ('costo', models.IntegerField(default=0)),
                ('id_almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Almacen')),
            ],
        ),
        migrations.CreateModel(
            name='Mago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energia', models.IntegerField(default='100')),
                ('damage_hechizos', models.IntegerField(default='10')),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('damage', models.IntegerField(default=1)),
                ('vida', models.IntegerField(default=0)),
                ('especialidad', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Personaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('velocidad_movimiento', models.DecimalField(decimal_places=2, max_digits=3)),
                ('aceleracion', models.DecimalField(decimal_places=2, max_digits=2)),
                ('vida', models.IntegerField(default='100')),
                ('defensa', models.IntegerField(default='0')),
                ('damage_ataque_basico', models.IntegerField(default='5')),
                ('salto', models.DecimalField(decimal_places=1, max_digits=1)),
                ('velocidad_ataque', models.DecimalField(decimal_places=2, max_digits=2)),
                ('estado', models.IntegerField(default='0')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, unique=True)),
                ('password', models.CharField(default='', max_length=100)),
                ('cash', models.IntegerField(default=0)),
                ('pais', models.CharField(default='Peru', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='personaje',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Usuario'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='id_personaje',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='General.Personaje'),
        ),
        migrations.AddField(
            model_name='mago',
            name='id_personaje',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='General.Personaje'),
        ),
        migrations.AddField(
            model_name='hechicero',
            name='id_personaje',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='General.Personaje'),
        ),
    ]
