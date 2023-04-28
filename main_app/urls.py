from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('skins/', views.skins_index, name='index'),
  path('skins/<int:skin_id>/', views.skins_detail, name='detail'),
  path('skins/create/', views.SkinCreate.as_view(), name='skins_create'),
  path('skins/<int:pk>/update/', views.SkinUpdate.as_view(), name='skins_update'),
  path('skins/<int:pk>/delete/', views.SkinDelete.as_view(), name='skins_delete'),
  path('skins/<int:skin_id>/add_used/', views.add_used, name='add_used'),
  path('skins/<int:skin_id>/assoc_buddy/<int:buddy_id>/', views.assoc_buddy, name='assoc_buddy'),
  path('skins/<int:skin_id>/unassoc_buddy/<int:buddy_id>/', views.unassoc_buddy, name='unassoc_buddy'),
  path('buddies/', views.BuddyList.as_view(), name='buddies_index'),
  path('buddies/<int:pk>/', views.BuddyDetail.as_view(), name='buddies_detail'),
  path('buddies/create/', views.BuddyCreate.as_view(), name='buddies_create'),
  path('buddies/<int:pk>/update/', views.BuddyUpdate.as_view(), name='buddies_update'),
  path('buddies/<int:pk>/delete/', views.BuddyDelete.as_view(), name='buddies_delete'),
]g