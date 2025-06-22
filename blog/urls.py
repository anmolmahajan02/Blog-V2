from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path('login', views.login ,name='login'),
    path('register', views.register ,name='register'),
    path('logout', views.logout ,name='logout'),
    path('yourPosts', views.yourPosts ,name='yourPosts'),
    path('addPost', views.addPost ,name='addPost'),
    path('fullPost/<str:pk>',views.fullPost,name='fullPost'),
    path('profile',views.profile,name='profile'),
]