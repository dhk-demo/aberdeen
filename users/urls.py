from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views

from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls
from two_factor.urls import urlpatterns as tf_urls
from django.conf.urls.static import static



from .views import (
    ExampleSecretView, HomeView, ConsentView, RegistrationView, ResetPasswordView, ChangePasswordView, profile,
)


urlpatterns = [
    path(
        '',
        HomeView.as_view(),
        name='home',
    ),
    path(
        'account/logout/',
        LogoutView.as_view(),
        name='logout',
    ),
    path(
        'secret/',
        ExampleSecretView.as_view(),
        name='secret',
    ),
    path(
        'account/register/',
        RegistrationView.as_view(),
        name='registration',
    ),
    path('', include(tf_urls)),
    path('', include(tf_twilio_urls)),
    path('', include('user_sessions.urls', 'user_sessions')),


    path('account/register/consent/', 
        ConsentView.as_view(),
        name='registration-consent',
    ),

     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

     path('password-change/', ChangePasswordView.as_view(), name='password_change'),

     
    # Add this
    path('profile/', profile, name='users-profile'),

    
     #Social login (google for now)
     re_path(r'^oauth/', include('social_django.urls', namespace='social')),



] 