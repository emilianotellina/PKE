from pke.csr import (
    FunctionNode,
    ClassNode,
    VariableNode,
    ParameterNode,
    ImportNode,
)


def test_function_node():

    fn = FunctionNode(
        "login",
        "login(user)",
        "bool"
    )


    assert fn.type == "function"

    assert fn.name == "login"

    assert fn.signature == "login(user)"

    assert fn.return_type == "bool"



def test_class_node():

    cls = ClassNode(
        "UserService",
        ["BaseService"]
    )


    assert cls.type == "class"

    assert cls.name == "UserService"



def test_variable_node():

    var = VariableNode(
        "counter",
        "int"
    )


    assert var.type == "variable"

    assert var.attributes["data_type"] == "int"



def test_parameter_node():

    param = ParameterNode(
        "user",
        "User"
    )


    assert param.type == "parameter"



def test_import_node():

    imp = ImportNode(
        "requests"
    )


    assert imp.type == "import"

    assert imp.name == "requests"