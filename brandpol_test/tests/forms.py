from .models import Tests, Questions
from django.forms import ModelForm, TextInput, Select

class TestsForm(ModelForm):
    class Meta:
        model = Tests
        fields = ['title', 'is_available']

        widget = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название теста'
            }),
            "is_available": Select(attrs={
                'class': 'form-control'
            })
        }

class QuestForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['test', 'question_text']

        widget = {
            "question_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название теста'
            })
        }

