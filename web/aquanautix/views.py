from django.views import generic

from .models import Artifact


class IndexView(generic.ListView):
    model = Artifact
    template_name = 'aquanautix/index.html'
    context_object_name = 'artifact_list'


class DetailView(generic.DetailView):
    model = Artifact
    template_name = 'aquanautix/detail.html'

