from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),   
    path('authors', views.authors),   
    path('create_book', views.create_book),   
    path('create_author', views.create_author),  
    path('show_book/<int:id>', views.show_book), 
    path('show_author/<int:id>', views.show_author), 
    path('add_author', views.add_author), 
    path('add_book', views.add_book), 
]