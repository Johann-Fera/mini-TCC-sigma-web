# Generated by Django 5.2.2 on 2025-06-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_comida_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dia', models.DateField(auto_now_add=True)),
                ('hora', models.TimeField(auto_now_add=True)),
                ('pessoas', models.PositiveIntegerField()),
                ('obs', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='comida',
            name='popular',
            field=models.BooleanField(default=False),
        ),
    ]
