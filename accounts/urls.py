from django.urls import path
from .views import RegisterView, LoginView, GuestLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('guest-login/', GuestLoginView.as_view(), name='auth_guest_login'),
]
