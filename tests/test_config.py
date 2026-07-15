from pke.core.config import ConfigManager


def test_default_config():

    manager = ConfigManager()

    config = manager.load()

    assert config.project is not None