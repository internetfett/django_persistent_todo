from django.contrib import admin

from django_persistent_todo.models import ToDoItem

class ToDoItemAdmin(admin.ModelAdmin):
    """ Register item admin for demonstration. """
    list_display = ('list_id', 'text')
    list_filter = ('complete',)
    search_fields = ('text',)

admin.site.register(ToDoItem, ToDoItemAdmin)    
