from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.views.generic.detail import SingleObjectMixin

from django_persistent_todo.forms import AddToDoForm
from django_persistent_todo.models import ToDoItem


class RedirectMixin(object):
    def get_success_url(self):
        """ Redirect to the origin. """
        return self.request.META.get('HTTP_REFERER','/')


class AddToDoView(RedirectMixin, FormView):
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


class DelToDoView(RedirectMixin, TemplateView, SingleObjectMixin):
    http_method_names = ['get']
    model = ToDoItem
    
    def get(self, request, *args, **kwargs):
        """ Delete existing todo item. """
        if self.get_object():
            self.get_object().delete()
        return HttpResponseRedirect(self.get_success_url())
