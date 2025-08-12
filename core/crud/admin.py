from django.contrib import admin
from crud.models import Item

# Register your models here.
@admin.register(Item)
class CrudAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'date_created']