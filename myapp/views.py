from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import MyModel
from .forms import MyModelForm


class Home(TemplateView):
    template_name = 'base.html'


class List(ListView):
    model = MyModel


class Create(CreateView):
    model = MyModel
    form_class = MyModelForm
    success_url = reverse_lazy('list')

class Update(UpdateView):
    model = MyModel
    form_class = MyModelForm
    success_url = reverse_lazy('list')
