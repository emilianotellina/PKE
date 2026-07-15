def test_plugin_imports():

    from pke.core.plugins import (
        PKEPlugin,
        PluginManager,
        PluginRegistry,
        PluginLoader,
    )

    assert PKEPlugin is not None
    assert PluginManager is not None
    assert PluginRegistry is not None
    assert PluginLoader is not None