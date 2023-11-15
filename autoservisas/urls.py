from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('uzsakymai/', views.UzsakymaiListView.as_view(), name='uzsakymai'),
    path('manouzsakymai/', views.KlientoUzsakymaiListView.as_view(), name='mano_uzsakymai'),
    path('kainynas/', views.kainynas, name='kainynas'),
    path('klientai/', views.klientai, name='klientai'),
    path('uzsakymai/<int:uzsakymas_id>', views.uzsakymas, name='uzsakymas'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
    path('search/', views.search, name='search'),
]