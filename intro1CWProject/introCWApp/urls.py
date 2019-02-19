from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='index'),
    path('wutang/', views.wutang, name='index'),
    path('fleetwoodmac/', views.fleetwoodmac, name='index'),
    path('shing02/', views.shing02, name='index'),
]