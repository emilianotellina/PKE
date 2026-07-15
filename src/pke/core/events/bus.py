class EventBus:

    def __init__(self):
        self._subscriptions = {}

    def subscribe(self, event_type, handler):

        self._subscriptions.setdefault(
            event_type,
            []
        ).append(handler)

    def unsubscribe(self, event_type, handler):

        if event_type in self._subscriptions:
            self._subscriptions[event_type].remove(handler)

    def publish(self, event):

        for handler in self._subscriptions.get(event.type, []):
            handler(event)

    def clear(self):
        self._subscriptions.clear()