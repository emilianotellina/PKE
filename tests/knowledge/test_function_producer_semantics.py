from pke.knowledge.producers.function import FunctionProducer
from pke.knowledge.function import Function, Parameter


def test_function_document_generation():

    function = Function(
        name="login",
        signature="login(user)"
    )


    function.parameters.append(
        Parameter("user")
    )


    function.variables.append(
        "token"
    )


    function.calls.append(
        "authenticate(user)"
    )


    function.returns.append(
        "token"
    )


    output = FunctionProducer().generate(
        function
    )


    assert "# login" in output

    assert "token" in output

    assert "authenticate(user)" in output

    assert "## Returns" in output