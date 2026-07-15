from pke.core.plugins import (
    PluginRegistry
)


class TestPlugin:

    name = "test"

    version = "1.0"



def test_registry():

    registry = PluginRegistry()

    plugin = TestPlugin()


    registry.register(
        plugin
    )


    assert registry.get(
        "test"
    ) == plugin