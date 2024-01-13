from django.db import models
from users import models as umodels
from django.views.generic import DeleteView
from django.contrib import admin
 
class TusksAdmin(admin.ModelAdmin):
    list_filter = ('date', 'title')

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Tusks(models.Model):
    title = models.CharField('Название задачи', max_length=50)                        
    tusk_description = models.TextField('Описание задачи', max_length=1500)            
    date = models.DateTimeField('дедлайн')
    tags = models.ManyToManyField(Tag) 
                                           
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Задача',
        verbose_name_plural = 'Задачи'


class TuskDeleteView(DeleteView):
    model= Tusks
    success_url = '/tusks/'
    template_name = 'task_delete.html'

class User_Tusks(models.Model):
    user_id = models.ForeignKey(umodels.User, on_delete = models.CASCADE,related_name='user_id')
    tusks_id = models.ForeignKey(Tusks, on_delete = models.CASCADE,related_name='tusks_id')
    
    def __str__(self):
        return f"{self.user_id}-->{self.tusks_id}"
    
    class Meta:
        verbose_name = 'Пользователи и задачи',
        verbose_name_plural = 'Пользователи и задачи'


class Task_Comment(models.Model):
    tusks_id = models.ForeignKey(Tusks, on_delete = models.CASCADE, related_name='comments')
    text_comment = models.TextField('Комментарий к задаче', max_length=500)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" {self.tusks_id}->{self.text_comment}"

    class Meta:
        verbose_name = 'Комментарии к задачам',
        verbose_name_plural = 'Комментарии к задачам'


