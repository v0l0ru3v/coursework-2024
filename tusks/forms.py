from django import forms
from .models import Tusks, Task_Comment, Tag
from django.forms import ModelForm,TextInput, DateTimeInput,Textarea, ModelMultipleChoiceField

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tusks
        fields = ['title', 'tusk_description', 'date','tags']

class TuskCreateForm(ModelForm):
    class Meta:
        model = Tusks
        tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        
    )
        fields = ['title', 'tusk_description', 'date','tags']
        
        widgets = {
            "title": TextInput(attrs={
                'placeholder': 'Название задачи',
            }),
            "tusk_description" : Textarea(attrs={
                'placeholder': 'Описание задачи',
                
            }),
            "date" : DateTimeInput(attrs={
                'placeholder': 'Дедлайн',
                'type': 'datetime-local'
            }),
            "tags": forms.CheckboxSelectMultiple(attrs={
                'placeholder': 'Хештеги',
                'required' : False,
            })
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Task_Comment
        fields = ['text_comment'] 