from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tabletScreen1', views.tabletScreen1, name='tabletScreen1'),
    path('tabletScreen2', views.tabletScreen2, name='tabletScreen2'),
    path('tabletScreen3', views.tabletScreen3, name='tabletScreen3'),
    path('orderList/', views.orderList, name='orderList'),
    path('createWork', views.createWork, name='createWork'),
    path('makeEdit/<int:pk>/', views.makeEdit, name='makeEdit'),
    path('finishedList', views.finishedList, name='finishedList'),

    path('workData/', views.workData, name='workData'),
    path('elapsedTime/', views.elapsedTime, name='elapsedTime'),
    path('workerID/', views.workerID, name='workerID'),
    path('stockLevel/', views.stockLevel, name='stockLevel'),
    path('workerCard/', views.workerCard, name='workerCard'),
    path('tabletState/', views.tabletState, name='tabletState'),

    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),


]

