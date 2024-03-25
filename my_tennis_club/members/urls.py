from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.tennis_members, name="members list"),
]
