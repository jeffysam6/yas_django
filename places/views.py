from django.shortcuts import render
from places.models import Park
from django.views.generic import TemplateView

class ParkView(TemplateView):
    template_name = 'places/park.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['park'] = Park.objects.get(pk=kwargs['pk'])
        return context

