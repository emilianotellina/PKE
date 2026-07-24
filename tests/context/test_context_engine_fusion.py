from pke.context.context_engine import ContextEngine


class FakeSymbol:

    def __init__(self, name):

        self.name = name

        self.type = "function"

        self.calls = []

        self.called_by = []

        self.dependencies = []

        self.side_effects = []

        self.metrics = {}



class FakeFile:

    def __init__(self):

        self.name = "login.py"

        self.symbols = [

            FakeSymbol("login")

        ]



class FakePackage:

    def __init__(self):

        self.name = "core"

        self.files = [

            FakeFile()

        ]



class FakeProject:

    name = "test_project"

    packages = [

        FakePackage()

    ]



def test_context_engine_contains_fusion():

    engine = ContextEngine()


    result = engine.build(

        project=FakeProject(),

        target="login"

    )


    assert "fusion" in result


    assert isinstance(

        result["fusion"],

        list

    )


    assert len(

        result["fusion"]

    ) == 1


    assert result["fusion"][0]["symbol"] == "login"