from django import template

from django_persistent_todo.forms import AddToDoForm
from django_persistent_todo.models import ToDoItem

register = template.Library()

@register.inclusion_tag('todo_list.html')
def display_todo_list(list_id):
    """ Lookup and display the list. """
    form = AddToDoForm()
    form.fields['list_id'].initial = list_id
    items = ToDoItem.objects.filter(list_id=list_id)
    return {'items': items, 'form': form}
