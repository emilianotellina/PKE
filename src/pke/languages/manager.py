from pathlib import Path


class LanguageManager:


    def __init__(self, registry):

        self.registry = registry



    def detect(self, file):

        file = Path(file)


        for plugin in self.registry.all():

            if plugin.detect(file):

                return plugin


        return None