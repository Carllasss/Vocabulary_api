from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views


urlpatterns = [
    path('categories/', views.CategoryView.as_view()),
    path('levels/', views.LevelView.as_view()),
    path('words/<int:pk>/', views.WordsView.as_view()),
    path('themes/', views.ThemesView.as_view({'get': 'list'})),
    path('themes/<int:pk>/', views.ThemesView.as_view({'get': 'retrieve'})),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)