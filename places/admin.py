from django.contrib import admin
from places.models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(PlaceImage)
class AdminPlaceImage(admin.ModelAdmin):
    pass