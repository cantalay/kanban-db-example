from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
   # path('makeEdit', views.makeEdit, name='makeEdit'),
    path('makeEdit/<int:pk>/', views.makeEdit, name='makeEdit'),
    path('tabletScreen', views.tabletScreen, name='tabletScreen'),
    path('createWork', views.createWork, name='createWork'),
    path('arduino', views.arduino, name='arduino'),
]
