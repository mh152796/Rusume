from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path('cv_creation', views.cv_creation, name="cv_creation"),
    path('cv_view/<str:pk>/', views.cv_view, name="cv_view"),
    path('delete-cv/<str:pk>/', views.delete_cv, name="delete-cv"),
]
