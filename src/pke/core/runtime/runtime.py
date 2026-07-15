from .container import ServiceContainer
from .registry import ComponentRegistry
from .lifecycle import LifecycleManager

from pke.core.events.bus import EventBus


class Runtime:

    def __init__(self):

        self.services = ServiceContainer()

        self.registry = ComponentRegistry()

        self.lifecycle = LifecycleManager()

        self.events = EventBus()

    def register(self, component):

        component.configure(self)

        self.registry.register(component)

    def start(self):

        components = self.registry.all()

        self.lifecycle.initialize(components)

        self.lifecycle.start(components)

    def stop(self):

        components = self.registry.all()

        self.lifecycle.stop(components)

        self.lifecycle.destroy(components)