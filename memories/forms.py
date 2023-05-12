from django import forms
from .models import Memory

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ('memory_name', 'memory_comment')
        widgets = {
            'memory_name': forms.TextInput(attrs={'class': 'memory-form-field'}),
            'memory_comment': forms.Textarea(attrs={'class': 'memory-form-field'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput()
        }
        labels = {
            'memory_name': 'Название воспоминания',
            'memory_comment': 'Комментарий'
        }
