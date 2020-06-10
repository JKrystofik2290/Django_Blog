from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        """Imports user signals for new user profile creation"""
        import users.signals
