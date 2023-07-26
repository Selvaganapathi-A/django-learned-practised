from django.apps import AppConfig


class App004Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_004"

    # def ready(self) -> None:
    #     from . import signals

    #     return super().ready()
