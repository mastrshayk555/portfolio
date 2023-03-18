from django.shortcuts import render
from django.views.generic import DetailView


class Home(DetailView):
    def get(self, request):
        return render(request, 'mysite/home.html')

class About(DetailView):
    def get(self, request):
        return render(request, 'mysite/about.html')

class Projects(DetailView):
    def get(self, request):
        return render(request, 'mysite/projects.html')
        
class Contact(DetailView):
    def get(self, request):
        return render(request, 'mysite/contact.html')

class Components(DetailView):
    def get(self, request):
        return render(request, 'mysite/components.html')
    
class GunViolence(DetailView):
    def get(self, request):
        return render(request, 'mysite/gun_violence.html')