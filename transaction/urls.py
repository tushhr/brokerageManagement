from django.urls import path, include

from . import views

app_name = 'transaction'

urlpatterns = [
    path('', views.index, name='index'),
    path('transaction/', views.transaction, name='transaction'),
]