from abc import ABC, abstractmethod


class PKEPlugin(ABC):


    name: str = "unknown"

    version: str = "0.0.0"



    @abstractmethod
    def initialize(self):
        pass



    @abstractmethod
    def start(self):
        pass



    @abstractmethod
    def stop(self):
        pass