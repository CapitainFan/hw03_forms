from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        labels = {'group': 'Группа', 'text': 'Напишите свой пост'}
        help_texts = {'group': 'Выберите группу', 'text': 'Введите ссообщение'}
        fields = ('text', 'group')
