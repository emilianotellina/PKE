from abc import ABC, abstractmethod


class KnowledgeProducer(ABC):


    @abstractmethod
    def generate(self, entity):

        pass