from django import forms

from django_persistent_todo.models import ToDoItem


class AddToDoForm(forms.ModelForm):
    """ Form for adding a new item to the list. """
    class Meta:
        exclude = ('order', 'complete')
        model = ToDoItem
