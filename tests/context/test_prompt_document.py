from pke.context.prompt_document import PromptDocument



def test_prompt_document_render():


    document = PromptDocument()


    document.add_section(
        "Task",
        "modifica login"
    )


    document.add_section(
        "Target",
        "login"
    )


    text = document.render()



    assert "# Task" in text

    assert "modifica login" in text

    assert "# Target" in text

    assert "login" in text