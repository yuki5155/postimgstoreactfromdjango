from django.forms import ModelForm
from .models import TodoApp


class TodoForms(ModelForm):
    class Meta:
        model= TodoApp
        fields = ('title', 'img',)