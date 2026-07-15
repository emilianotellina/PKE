from pke.core.runtime import Runtime, RuntimeComponent


class Demo(RuntimeComponent):

    def __init__(self):
        self.started = False

    def start(self):
        self.started = True


def test_runtime():

    runtime = Runtime()

    demo = Demo()

    runtime.register(demo)

    runtime.start()

    assert demo.started