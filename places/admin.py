from django.contrib import admin
from places.models import Place, PlaceImage
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    readonly_fields = (
        'get_preview',
    )
    fields = ('image', 'get_preview', 'index')

    def get_preview(self, instance):
        return format_html(
            '<img src="{url}" height="{height}" />',
            url = instance.image.url,
            height="200px",
        )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline, ]

@admin.register(PlaceImage)
class AdminPlaceImage(admin.ModelAdmin):
    pass