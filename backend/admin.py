from django.contrib import admin
from .models import *

# Register your models here.
class Categoria_Admin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class Message_Admin(admin.ModelAdmin):
    list_display = ('id', 'message', 'categoria')

    
admin.site.register(Categoria, Categoria_Admin)
admin.site.register(Message, Message_Admin)