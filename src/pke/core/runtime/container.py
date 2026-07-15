class ServiceContainer:

    def __init__(self):
        self._services = {}

    def register(self, service_type, instance):
        self._services[service_type] = instance

    def unregister(self, service_type):
        self._services.pop(service_type, None)

    def resolve(self, service_type):
        return self._services.get(service_type)

    def exists(self, service_type):
        return service_type in self._services

    def all(self):
        return dict(self._services)