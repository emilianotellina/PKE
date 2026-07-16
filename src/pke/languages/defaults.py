from .registry import LanguageRegistry

from .python import PythonLanguagePlugin



def create_default_registry():

    registry = LanguageRegistry()


    registry.register(
        PythonLanguagePlugin()
    )


    return registry