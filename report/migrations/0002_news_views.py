from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='просмотры'),
        ),
    ]
