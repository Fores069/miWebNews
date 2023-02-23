from .models import News
from django.forms import ModelForm,TextInput,Textarea,DateInput


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'author','date']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Заголовок'
            }),
            'description':Textarea(attrs={
                'class':'form-control'
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'type':'date'

            }),
            'author':TextInput(attrs={
                'class':'form-control',
                'placeholder':'Автор'
            })



        }