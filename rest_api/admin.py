from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Level, Words, Themes


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.get_url()}" style="max-height: 200px;">')


class ThemesAdmin(admin.ModelAdmin):
    fields = ['name', 'photo', 'preview', 'level', 'words', 'category']
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.get_url()}" style="max-height: 200px;">')

class WordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'translation', 'player')

    readonly_fields = ('player',)

    def player(self, obj):
        template = f'<audio controls>' \
                   f'<source src={obj.get_url()} type="audio/mpeg">' \
                   f'<source src={obj.get_url()} type="audio/ogg">'\
                   f'</audio>'
        return mark_safe(template)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Level)
admin.site.register(Words, WordsAdmin)
admin.site.register(Themes, ThemesAdmin)
