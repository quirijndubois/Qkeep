from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('notes/<int:pk>/update/', views.update_note, name='update_note'),
    path('notes/new/', views.new_note, name='new_note'),
]