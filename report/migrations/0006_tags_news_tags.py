from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0005_categories_slug_alter_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название тега')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='report.tags', verbose_name='теги'),
        ),
    ]
