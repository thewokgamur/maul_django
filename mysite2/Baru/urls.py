from django.urls import path
from . import views

app_name = 'Baru'

urlpatterns = [
    path('isinews',views.test, name='isinews')
]