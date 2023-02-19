# Generated by Django 4.1.7 on 2023-02-17 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('cantidad', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('ci', models.IntegerField(default=0)),
                ('base_monetaria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('precio_base', models.IntegerField(default=0)),
                ('disponible', models.BooleanField(blank=True, default=True)),
                ('moneda', models.CharField(choices=[('$', 'dolares'), ('Bs', 'bolivianos')], default='Bs', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subasta_producto.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pila_subasta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oferta', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('orden', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subasta_producto.subasta')),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subasta_producto.usuario')),
            ],
        ),
    ]