import importlib.util


class PluginLoader:


    def load(
        self,
        path
    ):


        spec = importlib.util.spec_from_file_location(
            "pke_plugin",
            path
        )


        module = importlib.util.module_from_spec(
            spec
        )


        spec.loader.exec_module(
            module
        )


        return module