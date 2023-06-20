from django.db import models

class Tusks(models.Model):
    title = models.CharField('Название задачи', max_length=50) #название задачи
    tusk_description = models.TextField('Описание задачи', max_length=1500)            #Полный текст задачи
    date = models.DateTimeField('дедлайн')           #Время начала           #Дедлайн
                
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tusk',
        verbose_name_plural = 'Tusks'
# Create your models here.
