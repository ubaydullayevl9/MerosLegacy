from django.contrib import admin
from .models import Teacher, Meros, Makom, Bolim, Shoba, Kuy


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_place', 'profession', 'created_at')
    list_filter = ('profession', 'birth_place')
    search_fields = ('full_name', 'biography', 'achievements')
    prepopulated_fields = {'slug': ('full_name',)}
    ordering = ['full_name']


@admin.register(Meros)
class MerosAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'teacher', 'created_at')
    list_filter = ('resource_type', 'teacher')
    search_fields = ('title', 'lyrics', 'description', 'teacher__full_name')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['title']

admin.site.register(Makom)
admin.site.register(Bolim)
admin.site.register(Shoba)
admin.site.register(Kuy)
