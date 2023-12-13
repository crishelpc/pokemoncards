from django.forms import ModelForm
from django import forms
from .models import Trainer, PokemonCard, Collection


class TrainerForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = Trainer
        fields = '__all__'
        
        
class PokemonCardForm(ModelForm):
    class Meta:
        model = PokemonCard
        fields = '__all__'