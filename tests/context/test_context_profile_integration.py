from pke.context.context_engine import ContextEngine
from pke.context.context_profile import ContextProfile



class FakeSymbol:

    def __init__(self, name):

        self.name = name

        self.calls = []

        self.called_by = []

        self.dependencies = []

        self.side_effects = []



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

    name = "test"

    packages = [

        FakePackage()

    ]



def test_context_engine_accepts_profile():


    engine = ContextEngine()


    profile = ContextProfile(

        name="debug",

        prioritize_risks=True

    )


    result = engine.build(

        project=FakeProject(),

        target="login",

        profile=profile

    )


    assert result is not None

    assert "fusion" in result

    assert len(result["fusion"]) == 1

    assert result["fusion"][0]["symbol"] == "login"