from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.authView, name='authView'),
    path("", views.go_home, name='home'), 
    path('accounts/login/', views.login_view, name='login'),
    path("accounts/", include("django.contrib.auth.urls")),
]
