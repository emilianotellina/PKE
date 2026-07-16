from pke.knowledge import (
    Package,
    SourceFile,
    Function,
    Parameter,
    PackageProducer,
    FileProducer,
    FunctionProducer,
)


def test_package_producer():

    package = Package(
        name="core"
    )


    package.files.append(
        SourceFile(
            name="test.py"
        )
    )


    result = PackageProducer().generate(
        package
    )


    assert "core" in result

    assert "test.py" in result



def test_file_producer():

    file = SourceFile(
        name="main.py",
        language="python"
    )


    result = FileProducer().generate(
        file
    )


    assert "main.py" in result



def test_function_producer():

    function = Function(
        name="hello",
        return_type="None"
    )


    result = FunctionProducer().generate(
        function
    )


    assert "hello" in result