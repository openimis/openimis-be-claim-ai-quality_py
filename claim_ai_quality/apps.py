from django.apps import AppConfig

MODULE_NAME = 'claim_ai_quality'

DEFAULT_CONFIG = {
    "claim_ai_url": "ws://localhost:8000/claim_ai/ws/Claim/process/",
    "event_based_activation": False,
    "bundle_size": 100,
    "zip_bundle": False,
    "connection_timeout": 5
}


class ClaimAiQualityConfig(AppConfig):
    name = MODULE_NAME

    claim_ai_url = DEFAULT_CONFIG["claim_ai_url"]
    event_based_activation = DEFAULT_CONFIG["event_based_activation"]
    bundle_size = DEFAULT_CONFIG["bundle_size"]
    zip_bundle = DEFAULT_CONFIG["zip_bundle"]
    connection_timeout = DEFAULT_CONFIG["connection_timeout"]

    def _configure_perms(self, cfg):
        for config, config_value in cfg.items():
            setattr(ClaimAiQualityConfig, config, config_value)

    def ready(self):
        from core.models import ModuleConfiguration
        cfg = ModuleConfiguration.get_or_default(MODULE_NAME, DEFAULT_CONFIG)
        self._configure_perms(cfg)
