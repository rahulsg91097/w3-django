from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path('members/', views.tennis_members, name="members list"),
    path('members/details/<int:id>', views.detail, name='Details'),
    path('testing', views.testing, name="Testing")
]
