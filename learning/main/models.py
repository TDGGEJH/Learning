from django.db import models

class Shodki(models.Model):
    title = models.CharField('Имя', max_length=15)
    location = models.CharField('Локация', max_length=50)
    desk = models.CharField('Описание', max_length=250)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Сходка"
        verbose_name_plural = "Сходки"