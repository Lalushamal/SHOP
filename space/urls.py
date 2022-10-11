from django.urls import URLPattern, path
from . import views


urlpatterns=[
    path('',views.index,name=''),
    path('home',views.home,name=''),
    path('product',views.product,name=''),
    path('about',views.about,name=''),
    path('help',views.help,name=''),

]