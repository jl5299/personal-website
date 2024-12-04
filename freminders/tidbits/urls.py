from django.urls import path
from . import views

urlpatterns = [
    path('', views.friends, name='friends'),
    # path('friendnote/', views.FriendNote, name='friendnote'),
    path('friendnotes/', views.FriendNoteListView.as_view(), name='friendnotes'),

]