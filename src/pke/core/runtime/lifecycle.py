class LifecycleManager:

    def initialize(self, components):
        for c in components:
            c.initialize()

    def start(self, components):
        for c in components:
            c.start()

    def stop(self, components):
        for c in reversed(components):
            c.stop()

    def destroy(self, components):
        for c in reversed(components):
            c.destroy()