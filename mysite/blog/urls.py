from django.urls import path
from . import views




app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]

