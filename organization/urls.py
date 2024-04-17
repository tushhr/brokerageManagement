from django.urls import path, include

from . import views

app_name = 'organization'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:org_id>', views.org_detail, name='org_detail')
]