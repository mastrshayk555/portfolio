from django.shortcuts import render
from django.views.generic import DetailView


class index(DetailView):
    def get(self, request):
        return render(request, 'mysite/index.html')