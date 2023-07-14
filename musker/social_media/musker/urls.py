from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/followers/<int:pk>/', views.followers, name='followers'),
    path('profile/follows/<int:pk>/', views.follows, name='follows'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update-user'),
    path('meep_like/<int:pk>/', views.meep_like, name='meep_like'),
    path('meep_show/<int:pk>/', views.meep_show, name='meep_show'),
    path('meep_delete/<int:pk>/', views.meep_delete, name='meep_delete'),
    path('meep_edit/<int:pk>/', views.meep_edit, name='meep_edit'),
    path('unfollow/<int:pk>/', views.unfollow_user, name='unfollow'),
    path('follow/<int:pk>/', views.follow_user, name='follow'),
    path('search/', views.search, name='search'),
    path('search_user/', views.search_user, name='search_user'),
]
