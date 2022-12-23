from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_news_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='дата добавление'),
        ),
    ]
