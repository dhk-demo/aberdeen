
import django_saml2_auth.views

from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls



urlpatterns = [
     path('admin/', admin.site.urls),

     #apps
     path('', include('users.urls')),
    
     path('forums/', include('forum.urls')),
     #login related urls

     path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

     path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

     path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

     path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    path('', include(tf_urls)),

    path('', include(tf_twilio_urls)),

     #For OKTA
     re_path(r'^saml2_auth/', include('django_saml2_auth.urls')),
     # The following line will rep
     # If you want to specific the after-login-redirect-URL, use parameter “?next=/the/path/you/want”
     # with this view.
     re_path(r'^accounts/login/$', django_saml2_auth.views.signin),
     # This will redirect to okta 
     re_path(r'^admin/login/$', django_saml2_auth.views.signin),

     re_path(r'^oauth/', include('social_django.urls', namespace='social')),

    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
