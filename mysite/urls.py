from django.urls import path
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('about', views.about.as_view(), name='about'),
    path('works', views.works.as_view(), name='works'),
    path('contact', views.contact.as_view(), name='contact'),
    path('components', views.components.as_view(), name='components'),
]