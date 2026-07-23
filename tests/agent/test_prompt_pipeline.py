from pke.agent.prompt import AgentPrompt
from pke.context.prompt_document import PromptDocument



def test_prompt_pipeline():


    document = PromptDocument()


    document.add_section(
        "Task",
        "modifica autenticazione"
    )


    document.add_section(
        "Target",
        "login"
    )


    prompt = AgentPrompt(

        task="modifica autenticazione",

        target="login",

        document=document

    )


    text = prompt.render()



    assert "# Task" in text

    assert "modifica autenticazione" in text

    assert "# Target" in text

    assert "login" in text