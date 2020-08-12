from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add_post/', views.add_post, name='add_post'),
    path('content/', views.post_list, name='post_list'),
    path('<slug:slug>/edit', views.post_edit, name='post_edit'),
    path('videos', views.videos, name='videos'),
    path('new_video/', views.add_video, name='add_video'),
    path('post/<slug:slug>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<slug:slug>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<slug:slug>/remove/', views.comment_remove, name='comment_remove'),
    path('post/<slug:slug>/comment/', views.add_comment_to_post, name='add_comment_to_video'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('draft', views.draft, name='draft_post'),

]
