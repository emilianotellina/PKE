from pke.csr import CSRBuilder


def test_builder_context_stack():

    builder = CSRBuilder()


    function = builder.begin_function(
        "test"
    )


    assert builder.current_context().type == "body"


    builder.end_function()


    assert builder.current_context() is None