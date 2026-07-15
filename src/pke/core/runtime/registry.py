class ComponentRegistry:

    def __init__(self):
        self._components = []

    def register(self, component):
        self._components.append(component)

    def all(self):
        return list(self._components)