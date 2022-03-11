from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayPapers, name='displayPapers'),
    path('add/', views.newPaper, name='newPaper'),
    path('<int:paperID>', views.displayPaper, name='displayPaper'),
    path('delete/<int:paperID>/', views.removePaper, name='removePaper'),
    path('edit/<int:paperID>/', views.editPaper, name='editPaper'),
]