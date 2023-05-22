from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
from django.db.models import Q

from .models import KierunekStudiow

class StronaGlownaView(View):
    def get(self, request):
        return render(request, 'index.html')

class WyszukiwarkaKierunkowView(View):
    def get(self, request):
        query = request.GET.get('query', '')

        kierunki = KierunekStudiow.objects.filter(Q(nazwa__icontains=query))

        context = {
            'query': query,
            'kierunki': kierunki
        }
        return render(request, 'search.html', context)

