from django.urls import path
from .views import HomePageView, TrainerList, TrainerCreateView, TrainerUpdateView, TrainerDeleteView
from cardquest import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer_list'),
    path('pokemon-card', TrainerList.as_view(), name='pokemon-card'),
    path('collection', TrainerList.as_view(), name='collection'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add'), 
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', TrainerDeleteView.as_view(), name='trainer-delete')
]