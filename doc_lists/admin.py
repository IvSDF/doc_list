from django.contrib import admin

from doc_lists.models import Direction, Doctor


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'sort_number', 'slug')
    list_display_links = ('sort_number', 'title')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'years_of_experience', 'slug', 'display_directions', 'sort_number',)
    list_display_links = ('sort_number', 'title')
    search_fields = ('title',)
    list_filter = ('directions',)
    filter_horizontal = ('directions', )

