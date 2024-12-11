from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'exam_project1_1.accounts'

    def ready(self):
        import exam_project1_1.accounts.signals
        