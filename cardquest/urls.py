from django.urls import path
from cardquest import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'), 
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'), 
  
    path('pokemon_card', views.PokemonCardListView.as_view(), name='pokemon-card'),
    path('pokemon_card/add', views.PokemonCardCreateView.as_view(), name='pokemon-card-add'),
    path('pokemon_card/<pk>', views.PokemonCardUpdateView.as_view(), name='pokemon-card-update'), 
    path('pokemon_card/<pk>/del', views.PokemonCardDeleteView.as_view(), name='pokemon-card-delete'),

    path('collection', views.CollectionList.as_view(), name='collection'),
    path('collection/add', views.CollectionCreateView.as_view(), name='collection-add'),
    path('collection/<pk>', views.CollectionUpdateView.as_view(), name='collection-update'), 
    path('collection/<pk>/del', views.CollectionDeleteView.as_view(), name='collection-delete'),
]
