from django import forms

from .models import City


class CityForm(forms.ModelForm):
    name = forms.CharField(
        label='Город',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Название города',
            })
    )

    class Meta(object):
        model = City
        fields = ('name',)
