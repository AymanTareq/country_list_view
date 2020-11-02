from django.db import models

class country_info(models.Model):
    country_name = models.CharField(max_length=25)
    short_description = models.CharField(max_length=256)
    wiki_link = models.URLField(help_text='Provide a link to know more...')
    country_flag = models.ImageField()
