from django.urls import path
from.import views


urlpatterns = [
    path('ad/', views.addBlogView, name='addblog_url'),
    path('sh/', views.showBlogView, name='showblog_url'),
    path('up/<int:pk>/', views.updateBlogView, name='updateblog_url'),
    path('dl/<int:pk>/', views.deleteBlogView, name='deleteblog_url')
]