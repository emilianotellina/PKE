from pke.core.runtime import ServiceContainer


def test_register():

    c = ServiceContainer()

    obj = object()

    c.register(str, obj)

    assert c.resolve(str) is obj