from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModerationConfig(AppConfig):
    name = "djangocms_moderation"
    verbose_name = _("django CMS Moderation")

    def ready(self):
        import djangocms_moderation.handlers  # noqa: F401
        import djangocms_moderation.monkeypatch  # noqa: F401
        import djangocms_moderation.signals  # noqa: F401
