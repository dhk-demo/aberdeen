from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import iamsmartProvider


urlpatterns = default_urlpatterns(iamsmartProvider)