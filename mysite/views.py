from django.shortcuts import render
from django.views.generic import DetailView


class home(DetailView):
    def get(self, request):
        return render(request, 'mysite/home.html')

class about(DetailView):
    def get(self, request):
        return render(request, 'mysite/about.html')

class works(DetailView):
    def get(self, request):
        return render(request, 'mysite/projects.html')
        
class contact(DetailView):
    def get(self, request):
        return render(request, 'mysite/contact.html')

class components(DetailView):
    def get(self, request):
        return render(request, 'mysite/components.html')