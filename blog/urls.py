from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('new_post/', views.add_post, name='add_post'),
    path('content/', views.post_list, name='post_list'),
    path('<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('videos', views.videos, name='videos'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),

]