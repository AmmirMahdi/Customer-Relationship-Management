# Generated by Django 3.1.7 on 2021-03-02 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Contact', '0001_initial'),
        ('Account', '0002_auto_20210302_1524'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Opportinuty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('stage', models.CharField(choices=[('QUALIFICATION', 'QUALIFICATION'), ('NEEDS ANALYSIS', 'NEEDS ANALYSIS'), ('VALUE PROPOSITION', 'VALUE PROPOSITION'), ('ID.DECISION MAKERS', 'ID.DECISION MAKERS'), ('PERCEPTION ANALYSIS', 'PERCEPTION ANALYSIS'), ('PROPOSAL/PRICE QUOTE', 'PROPOSAL/PRICE QUOTE'), ('NEGOTIATION/REVIEW', 'NEGOTIATION/REVIEW'), ('CLOSED WON', 'CLOSED WON'), ('CLOSED LOST', 'CLOSED LOST')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('lead_souce', models.CharField(max_length=50)),
                ('probility', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Account.account')),
                ('closed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contacts', models.ManyToManyField(to='Contact.Contact')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by_opportinuty', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
