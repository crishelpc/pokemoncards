from django.contrib import admin
from . import models


@admin.register(models.Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email", "created_at", "updated_at")
    search_fields = ("name", "location",)

@admin.register(models.PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity", "hp", "card_type", "attack", "description", "weakness", "card_number", "release_date", "evolution_stage", "abilities", "created_at", "updated_at")
    search_fields = ("name",)

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("card", "trainer", "collection_date", "created_at", "updated_at")
    search_fields = ("card", "trainer")