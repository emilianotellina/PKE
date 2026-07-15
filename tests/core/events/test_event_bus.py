from pke.core.events import EventBus, Event


def test_publish():

    received = []

    bus = EventBus()

    bus.subscribe(
        "test",
        lambda e: received.append(e)
    )

    bus.publish(
        Event(
            type="test",
            source="pytest"
        )
    )

    assert len(received) == 1