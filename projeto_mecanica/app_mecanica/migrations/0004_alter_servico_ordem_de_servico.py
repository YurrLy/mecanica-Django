# Generated by Django 4.2.8 on 2023-12-07 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_mecanica', '0003_alter_peca_ordem_de_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='ordem_de_servico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_mecanica.ordemdeservico'),
        ),
    ]
