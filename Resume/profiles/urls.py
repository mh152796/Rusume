from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
        path('login/', views.loginUser, name='login'),
        path('logout/', views.logoutUser, name='logout'),
        path('register/', views.registerUser, name='register'),
        path('account/', views.userAccount, name="account"),
        path('edit-account/', views.editAccount, name='edit-account'),
         path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),
         name="reset_password"),

        path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),
         name="password_reset_done"),

        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),
         name="password_reset_confirm"),

        path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),
         name="password_reset_complete"),
        path('activate/<uidb64>/<token>/',views.activate, name="activate"),
]     