from django.apps import AppConfig


class FollowersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'followers'

    def ready(self):
        """
        The ready method is called when the application is loaded.
        Import the signals module to register the signal handlers.
        """
        import followers.signals
