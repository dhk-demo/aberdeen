from django.urls import path
from .views import home, profile, consent, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('register/consent/', consent, name='users-register-consent'),
    path('profile/', profile, name='users-profile'),
]
