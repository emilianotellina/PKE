from .registry import PluginRegistry
from .loader import PluginLoader



class PluginManager:


    def __init__(self):

        self.registry = PluginRegistry()

        self.loader = PluginLoader()



    def discover(self, directory):

        return []



    def load(self, path):

        module = self.loader.load(path)


        plugin = module.plugin


        self.registry.register(
            plugin
        )


        return plugin



    def start_all(self):

        for plugin in self.registry.all():

            plugin.initialize()

            plugin.start()



    def stop_all(self):

        for plugin in self.registry.all():

            plugin.stop()