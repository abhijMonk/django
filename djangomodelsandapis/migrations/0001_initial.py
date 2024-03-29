# Generated by Django 4.0.2 on 2022-02-15 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('UF', 'UNCLASSIFIED'), ('AD', 'AUDIO'), ('VD', 'VIDEO'), ('XT', 'TEXT')], default='UF', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('types', models.CharField(choices=[('PR', 'PREGNANCY'), ('AB', 'BABY'), ('KD', 'KIDS'), ('BT', 'BEAUTY'), ('ML', 'MUMSLIFE'), ('TR', 'TRAVEL'), ('RC', 'RECIPES'), ('HL', 'HEALTH')], default='PR', max_length=2)),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangomodelsandapis.author')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=5000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangomodelsandapis.author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangomodelsandapis.blog')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangomodelsandapis.category')),
            ],
        ),
    ]
