# Generated by Django 5.1.6 on 2025-02-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=11, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('pagamento_em_dia', models.BooleanField(default=True)),
                ('queixa', models.CharField(choices=[('TDAH', 'TDAH'), ('Depressão', 'Depressão'), ('Ansiedade', 'Ansiedade'), ('Estresse', 'Estresse'), ('Transtorno Bipolar', 'Transtorno Bipolar'), ('Esquizofrenia', 'Esquizofrenia')], max_length=255)),
            ],
        ),
    ]
