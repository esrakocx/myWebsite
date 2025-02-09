from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('starter/', views.starter_page, name='starter'),
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-detail/', views.portfolio_detail, name='portfolio-detail'),
    path('blog/', views.post_list, name='post_list'),
]