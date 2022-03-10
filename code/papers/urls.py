from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayPapers, name='displayPapers'),
    path('<int:paperID>', views.displayPaper, name='displayPaper'),
    path('delete/<int:paperID>/', views.removePaper, name='removePaper'),
]