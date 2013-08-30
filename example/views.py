from django.views.generic import TemplateView


class ExampleView(TemplateView):
    """ View to display the template tag. """
    template_name = "example.html"
