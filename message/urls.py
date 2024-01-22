from django.urls import path
from . import views

urlpatterns = [
    path('messages', views.MessageAPI.as_view()),
    path('messages/<str:username>', views.MessageAPI.as_view()),
    path('sign-up', views.CreateUser.as_view()),
    path('login', views.LoginUser.as_view()),
    path('logout', views.LogoutUser.as_view()),
    path('update-details', views.UpdateUserDetails.as_view()),
    path('refresh-token', views.TokenRefreshView.as_view()),
    # path('forgot-password', views.ForgotPassword.as_view()),
]