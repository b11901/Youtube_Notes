from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('search/', views.search, name="search"),
    path('video/<slug:link>', views.video, name="video"),
    path('video/save_note/', views.saveNote, name="note"),
    path('video/<slug:link>/like', views.likeVideo, name="like"),
   # path('video/<slug:link>/add_to_playlist', views.likeVideo, name="add_to_playlist"),
    path('test/', views.test, name="test"),


]
