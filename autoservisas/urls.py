from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai'),
    path('kainynas/', views.kainynas, name='kainynas'),
    path('klientai/', views.klientai, name='klientai'),
    path('uzsakymai/', views.UzsakymaiListView.as_view(), name='uzsakymai'),
    path('manouzsakymai/', views.KlientoUzsakymaiListView.as_view(), name='mano_uzsakymai'),
    path('uzsakymai/<int:pk>', views.UzsakymasDetailView.as_view(), name='uzsakymas'),
    path('uzsakymai/new', views.UzsakymasCreateView.as_view(), name='naujas_uzsakymas'),
    path('uzsakymai/<int:pk>/update', views.UzsakymasUpdateView.as_view(), name='uzsakymas_update'),
    path('uzsakymai/<int:pk>/delete', views.UzsakymasDeleteView.as_view(), name='uzsakymas_delete'),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name='automobilis'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('profilis/', views.profilis, name='profilis'),
    path('i18n/', include('django.conf.urls.i18n')),
]
