from django.db import models

# Create your models here.

class ExplorerSite(models.Model):
    web_url = models.CharField(max_length=100, verbose_name="web URL")
    fs_path = models.CharField(max_length=200, verbose_name="Filesystem Path")
    
    def __str__(self):
        return self.web_url
    
    class Admin:
        list_display = ('web_url','fs_path',)
        ordering = ('web_url',)