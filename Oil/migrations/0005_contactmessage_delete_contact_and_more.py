# Generated by Django 5.1.7 on 2025-03-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oil', '0004_contact_updated_at_alter_oilproduct_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(default='Groundnut', max_length=100)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='oilproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='oilproduct',
            name='quantity',
        ),
        migrations.AddField(
            model_name='oilproduct',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
