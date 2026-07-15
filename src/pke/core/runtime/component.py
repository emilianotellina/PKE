from abc import ABC


class RuntimeComponent(ABC):

    def configure(self, runtime):
        pass

    def initialize(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def destroy(self):
        pass