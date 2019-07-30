from django.urls import path
from . import views

urlpatterns = [
    path("", views.profile_index, name="profile_index"),
    path("<int:pk>/", views.profile_detail, name="profile_detail"),
]