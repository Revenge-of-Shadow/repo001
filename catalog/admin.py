from django.contrib import admin

from .models import Author, Genre, Game, GameInstance, Language

#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(Game)
#admin.site.register(GameInstance)
admin.site.register(Language)
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
@admin.register(GameInstance)
class GameInstanceAdmin(admin.ModelAdmin):
    list_display = ('game', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields':('game', 'imprint', 'id')
        }),
        ('Availability', {
            'fields':('status', 'due_back', 'borrower')
        }),
    )
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'death_date')
