# Generated by Django 5.0.3 on 2024-03-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('documento', models.IntegerField()),
                ('ficha', models.IntegerField()),
                ('photo', models.ImageField(upload_to='fotos_aprendices')),
            ],
        ),
    ]
