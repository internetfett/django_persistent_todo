from django.views.generic import FormView

from django_persistent_todo.forms import AddToDoForm
from django_persistent_todo.models import ToDoItem


class AddToDoView(FormView):
    form_class = AddToDoForm
    http_method_names = ['post']
    
    def form_valid(self, form):
        """ Save the new todo item. """
        text = form.cleaned_data.get('text')
        item = ToDoItem(text=text)
        print vars(self)
        item.list_id = form.cleaned_data.get('list_id')
        item.save()
        return super(AddToDoView, self).form_valid(form)
        
    def get_success_url(self):
        """ Redirect to the origin. """
        return self.request.META.get('HTTP_REFERER','/')
