from django.contrib import admin

from .models import Achievement, AchievementCat, Cat

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)

class AchievementCatAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'cat',)

class CatAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'color', 'birth_year', 
        'owner', 'image',)

admin.site.register(Achievement, AchievementAdmin)
admin.site.register(AchievementCat, AchievementCatAdmin)
admin.site.register(Cat, CatAdmin)
