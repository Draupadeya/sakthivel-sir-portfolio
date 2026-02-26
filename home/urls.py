from django.urls import path
from . import views

urlpatterns = [
    # Public URLs
    path('', views.home, name='home'),
    path('achievements/', views.achievements, name='achievements'),
    path('gallery/', views.gallery, name='gallery'),
    path('awards/', views.awards, name='awards'),
    path('contact/', views.contact, name='contact'),
    path('cv/', views.cv, name='cv'),
    
    # Admin URLs
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    # Gallery Management
    path('admin/gallery/', views.gallery_list, name='gallery_list'),
    path('admin/gallery/add/', views.gallery_add, name='gallery_add'),
    path('admin/gallery/<int:pk>/edit/', views.gallery_edit, name='gallery_edit'),
    path('admin/gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),
    
    # Achievement Management
    path('admin/achievement/', views.achievement_list, name='achievement_list'),
    path('admin/achievement/add/', views.achievement_add, name='achievement_add'),
    path('admin/achievement/<int:pk>/edit/', views.achievement_edit, name='achievement_edit'),
    path('admin/achievement/<int:pk>/delete/', views.achievement_delete, name='achievement_delete'),
    
    # Award Management
    path('admin/award/', views.award_list, name='award_list'),
    path('admin/award/add/', views.award_add, name='award_add'),
    path('admin/award/<int:pk>/edit/', views.award_edit, name='award_edit'),
    path('admin/award/<int:pk>/delete/', views.award_delete, name='award_delete'),
    
    # CV Management
    path('admin/cv/', views.cv_list, name='cv_list'),
    path('admin/cv/add/', views.cv_add, name='cv_add'),
    path('admin/cv/<int:pk>/delete/', views.cv_delete, name='cv_delete'),
    
    # Profile Management
    path('admin/profile/edit/', views.profile_edit, name='profile_edit'),
]
