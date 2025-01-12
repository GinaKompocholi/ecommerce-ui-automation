import pytest

from ui_automation_suite.settings.config import AppEnvSettings


@pytest.fixture(scope="session")
def app_env_settings():
    aes = AppEnvSettings()
    return aes
