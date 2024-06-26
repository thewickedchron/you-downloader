from django.urls import path
from . import views

urlpatterns = [
    path("", views.yousingle), 
    path("video_page/", views.yousinglepage, name="video_page"), 
    path("<str:theid>", views.download, name="download")
]