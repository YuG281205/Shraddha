from django.urls import path
from . import views

urlpatterns = [
    path('', views.oil_list, name='oil_list'),
    path('add/', views.add_oil, name='add_oil'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact_us, name='contact_us'),
    path('update/<int:id>/', views.update_contact, name='update_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
]
