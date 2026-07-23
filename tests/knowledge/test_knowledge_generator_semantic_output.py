from pathlib import Path

from pke.knowledge.generator import KnowledgeGenerator


class FakeSideEffect:


    def __init__(
        self,
        effect_type
    ):

        self.type = effect_type



class FakeDependency:


    def __init__(
        self,
        name
    ):

        self.name = name

        self.type = name


class FakeFunction:


    def __init__(
        self,
        name
    ):

        self.name = name

        self.calls = [
            "authenticate"
        ]

        self.called_by = [
            "api_login"
        ]

        self.references = [
            "User"
        ]

        self.dependencies = [

            FakeDependency(
                "Database"
            )

        ]

        self.side_effects = [

            FakeSideEffect(
                "database_write"
            )

        ]

        self.complexity = 5



class FakeFile:


    def __init__(
        self,
        name,
        symbols
    ):

        self.name = name

        self.symbols = symbols



class FakePackage:


    def __init__(
        self,
        name,
        files
    ):

        self.name = name

        self.files = files



class FakeProject:


    def __init__(self):

        self.name = "test_project"

        self.packages = [

            FakePackage(

                "auth",

                [

                    FakeFile(

                        "login.py",

                        [

                            FakeFunction(
                                "login"
                            )

                        ]

                    )

                ]

            )

        ]



def test_knowledge_generator_writes_semantic_function_output(
    tmp_path
):


    project = FakeProject()


    generator = KnowledgeGenerator(
        tmp_path
    )


    generator.generate(
        project
    )


    function_file = (

        Path(tmp_path)

        /

        "test_project"

        /

        "auth"

        /

        "login.py"

        /

        "login.md"

    )


    assert function_file.exists()



    content = function_file.read_text(
        encoding="utf-8"
    )



    assert "# Function: login" in content

    assert "## Dependencies" in content

    assert "Database" in content

    assert "database_write" in content
