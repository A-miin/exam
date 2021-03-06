from django import forms

from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('name', 'email', 'text')


class RecordSearchForm(forms.Form):
    name = forms.CharField(max_length=128, label = "Введите имя")