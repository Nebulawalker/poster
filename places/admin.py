from django.contrib import admin
from places.models import Place, PlaceImage
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = (
        'get_preview',
    )
    fields = ('image', 'get_preview', 'index')
    extra = 0

    def get_preview(self, instance):
        return format_html(
            '<img src="{url}" height="{height}" />',
            url = instance.image.url,
            height="200px",
        )

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline, ]

@admin.register(PlaceImage)
class AdminPlaceImage(admin.ModelAdmin):
    pass