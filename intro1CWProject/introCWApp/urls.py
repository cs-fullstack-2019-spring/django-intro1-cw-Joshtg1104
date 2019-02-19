from django.urls import path

from . import views
# the paths to the three routes attached to the music routes
urlpatterns = [
    path('', views.index, name='index'),
    path('music/', views.music, name='index'),
    path('wutang/', views.wutang, name='index'),
    path('fleetwoodmac/', views.fleetwoodmac, name='index'),
    path('shing02/', views.shing02, name='index'),
]