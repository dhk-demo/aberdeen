from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class iamsmartAccount(ProviderAccount):
    def to_str(self):
        dflt = super(iamsmartAccount, self).to_str()
        return self.account.extra_data.get("name", dflt)


class iamsmartProvider(OAuth2Provider):
    id = "iamsmart"
    name = "iamsmart"
    account_class = iamsmartAccount

    def get_default_scope(self):
        return ["openid", "profile", "email", "offline_access"]

    def extract_uid(self, data):
        return str(data["preferred_username"])

    def extract_extra_data(self, data):
        return data

    def extract_email_addresses(self, data):
        return [
            EmailAddress(
                email=data["email"], verified=bool(data["email_verified"]), primary=True
            )
        ]

    def extract_common_fields(self, data):
        return dict(
            email=data["email"],
            last_name=data["family_name"],
            first_name=data["given_name"],
        )


provider_classes = [iamsmartProvider]