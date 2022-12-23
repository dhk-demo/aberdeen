import requests

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import iamsmartProvider


class iamsmartOAuth2Adapter(OAuth2Adapter):
    provider_id = iamsmartProvider.id

    settings = app_settings.PROVIDERS.get(provider_id, {})
    iamsmart_base_url = settings.get("iamsmart_BASE_URL")

    @property
    def access_token_url(self):
        return "https://{}/oauth2/v1/token".format(self.iamsmart_base_url)

    @property
    def authorize_url(self):
        return "https://{}/oauth2/v1/authorize".format(self.iamsmart_base_url)

    @property
    def userinfo_url(self):
        return "https://{}/oauth2/v1/userinfo".format(self.iamsmart_base_url)

    @property
    def access_token_method(self):
        return "POST"

    def complete_login(self, request, app, token, **kwargs):
        """
        Get the user info from userinfo endpoint and return a
        A populated instance of the `SocialLogin` model (unsaved)
        :param request:
        :param app:
        :param token:
        :param kwargs:
        :return:
        """

        resp = requests.get(
            self.userinfo_url,
            headers={"Authorization": "Bearer {}".format(token.token)},

        )

        resp.raise_for_status()
        extra_data = resp.json()
        login = self.get_provider().sociallogin_from_response(request, extra_data)
        return login


oauth2_login = OAuth2LoginView.adapter_view(iamsmartOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(iamsmartOAuth2Adapter)