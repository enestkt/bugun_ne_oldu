from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('news_list/', views.news_list, name='news_list'),
    path('category/<int:id>/', views.category, name='category'),
    path('news/<int:id>/', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
