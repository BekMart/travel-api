from django.apps import AppConfig


class CommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'

    def ready(self):
        """
        The ready method is called when the application is loaded.
        Import the signals module to register the signal handlers.
        """
        import comments.signals
