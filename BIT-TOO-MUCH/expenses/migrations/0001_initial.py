# Generated by Django 2.0.5 on 2018-08-29 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_expired', models.DateField()),
                ('final_value', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('is_paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['date_expired'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bills', to='expenses.BillCategory'),
        ),
    ]
