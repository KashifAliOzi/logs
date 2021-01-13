from django.contrib import admin
from django.urls import path, include
from . import views
from django_email_verification import urls as mail_urls


app_name = 'socialapp'
urlpatterns = [
    path('', views.registerPage),
    path('login/', views.userLogin, name="login"),
    path('registration_page/', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name="logout"),
    path('newpost/', views.newPost, name="newpost"),
    path('userpostspage/', views.userPostsPage, name='userposts'),
    path('postdetailpage/<int:id>', views.postdetail, name='postdetail'),
    path('updatepost/<int:id>/', views.updatePost, name='updatepost'),
    path('deletepost/<int:id>/', views.deletePost, name='deletepost'),
    path('verifylogin/', views.verifyEmail),


]
