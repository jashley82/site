from django.views import generic


class TemplateView(generic.base.TemplateView):
    template_name = 'mysite/index.html'
 
