# Generated by Django 3.1 on 2020-10-30 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('perfis', '0002_auto_20201029_0336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=255)),
                ('data_postagem', models.DateTimeField(auto_now_add=True)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Postagens', to='perfis.perfil')),
            ],
        ),
    ]
