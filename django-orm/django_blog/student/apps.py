from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudentConfig(AppConfig):
    name = 'django_blog.student'
    verbose_name = _("Student")

    def ready(self):
        try:
            import django_blog.student.signals  # noqa: F401
        except ImportError:
            pass
