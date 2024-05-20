# Generated by Django 5.0.4 on 2024-05-20 01:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_receta_usuario_alter_comentario_receta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planeacionsemanal',
            name='comida_del_dia',
        ),
        migrations.AddField(
            model_name='planeacionsemanal',
            name='usuario',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='receta',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recetas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ComidasPlaneacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comidasplaneacion_cena', to='app.receta')),
                ('colacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comidasplaneacion_colacion', to='app.receta')),
                ('colacion2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comidasplaneacion_colacion2', to='app.receta')),
                ('comida', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comidasplaneacion_comida', to='app.receta')),
                ('desayuno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comidasplaneacion_desayuno', to='app.receta')),
            ],
        ),
        migrations.AddField(
            model_name='planeacionsemanal',
            name='comidas_del_dia',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.comidasplaneacion'),
        ),
    ]
