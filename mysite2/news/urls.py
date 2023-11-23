from django.urls import path
from.import views

app_name = 'news'

urlpatterns = [
    path('tranding',views.tranding, name='tranding'),
    path('topik',views.topik, name='topik'),
    path('Shoping',views.Shoping, name='shoping'),
    path('News',views.News, name='News'),
    path('Berita',views.Berita, name='Berita'),
    path('Acation',views.Acation, name='Acation'),
    path('profile',views.profile, name='profile'),
    path('all',views.all, name='all'),

]