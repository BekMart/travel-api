from django.apps import AppConfig


class LikesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'likes'

    def ready(self):
        """
        The ready method is called when the application is loaded.
        Import the signals module to register the signal handlers.
        """
        import likes.signals
