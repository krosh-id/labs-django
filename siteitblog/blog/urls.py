from django.contrib import admin
from django.urls import path, register_converter
from . import converters
from .views import usefully_resource, LentaView, \
    ShowPostView, ShowMyPostsView, ShowByCategoryView, ProfileView, forms, video

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', LentaView.as_view(), name='lenta'),
    path('post/<int:post_id>', ShowPostView.as_view(), name='post'),
    path('category/<slug:cat_slug>', ShowByCategoryView.as_view(), name='category'),
    path('my-post/<int:profile_id>', ShowMyPostsView.as_view(), name='my-post'),
    path('profile/<int:profile_id>', ProfileView.as_view(), name='profile'),
    path('usefully-resource', usefully_resource, name='resource'),
    path('forms', forms, name='forms'),
    path('video', video, name='video'),
]
