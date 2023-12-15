from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Trainer, PokemonCard, Collection
from .forms import TrainerForm, PokemonCardForm, CollectionForm
from django.urls import reverse_lazy
import json


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 9

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')
    

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')
    
class PokemonCardListView(ListView):
    model = PokemonCard
    context_object_name = 'pokemoncard'
    template_name = "pokemon_cards.html"
    paginate_by = 3
    json_file_path = 'data/pokemon_data.json'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pokemon_data = self.get_pokemon_data()
        context['pokemon_data'] = pokemon_data
        return context
    
    def get_pokemon_data(self):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            return data.get('pokemons', [])
        
class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card-add.html'
    success_url = reverse_lazy('pokemon-card')

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card-edit.html'
    success_url = reverse_lazy('pokemon-card')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemon-card-del.html'
    success_url = reverse_lazy('pokemon-card')

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collections.html'
    paginate_by = 10

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection-add.html'
    success_url = reverse_lazy('collection')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection-edit.html'
    success_url = reverse_lazy('collection')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection-del.html'
    success_url = reverse_lazy('collection')