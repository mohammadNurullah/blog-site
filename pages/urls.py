from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('archives/',views.archives, name='archives'),
    path('posts/',views.posts, name='posts'),
    path('contact/',views.contact, name='contact'),
  # path('<int:listing_id>',views.listing, name='listing'),
]